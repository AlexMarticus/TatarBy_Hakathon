import datetime
import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from api_control import getUsers, getUserWords, changeWordLevel
from loader import dp, bot
from states.training import Questions


async def change_dates(state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']  # +
        need_words = data['ref3']  # +-
        user_id = data['ref2']
        id = data['ref5']
    for i in need_words:
        print(i)
        translate = ''
        flag = False
        for j in words_in_use:
            if i[1] == j[0]:
                flag = True
                translate = j[1]
        if not flag:
            print(datetime.datetime.strptime(i[3].split(' ')[0], "%Y-%m-%d") +
                  datetime.timedelta(days=1))
            await changeWordLevel(user_id=user_id, word_id=i[0],
                                  date=str(datetime.datetime.strptime(i[3].split(' ')[0], "%Y-%m-%d") +
                                           datetime.timedelta(days=1)), word_level=i[4])
        else:
            lvl = int(i[4]) + 1
            if int(i[4]) == 0:
                days = 0
            elif int(i[4]) == 1:
                days = 0
            elif int(i[4]) == 2:
                days = 3
            elif int(i[4]) == 3:
                days = 7
            elif int(i[4]) == 4:
                days = 15
            elif int(i[4]) == 5:
                days = 30
            elif int(i[4]) == 6:
                days = 30
            elif int(i[4]) == 7:
                days = 60
            else:
                days = 120
            if translate != i[2]:
                await bot.send_message(chat_id=id, text=f'Неверный перевод слова {i[1]}: введено-{translate}, '
                                                        f'верное-{i[2]}')
                days = 0
                lvl = 0
            res = await changeWordLevel(word_id=i[0], user_id=user_id,
                                        date=str(datetime.datetime.strptime(i[3].split(' ')[0], "%Y-%m-%d") +
                                                 datetime.timedelta(days=days)), word_level=lvl)
            print(res)


async def get_random_word(user_id, state: FSMContext, flag=False):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    if flag:
        all_users = await getUsers()
        user = False
        for i in all_users:
            if all_users[i]["telegram_id"] == user_id:
                user = i
                async with state.proxy() as data:
                    data['ref2'] = user
                break
        all_user_words = await getUserWords(user)
        need_words = []
        for i in all_user_words:
            if not ('date' not in all_user_words[i]):
                if datetime.datetime.strptime(all_user_words[i]['date'].split(' ')[0], "%Y-%m-%d") == \
                    str(datetime.date.today()) or all_user_words[i]['date'] is None:
                    if datetime.datetime.strptime(all_user_words[i]['date'].split(' ')[0], "%Y-%m-%d") == \
                        str(datetime.date.today()):
                        need_words.append(
                            [i, all_user_words[i]['word'], all_user_words[i]['word_ru'], all_user_words[i]['date'],
                             all_user_words[i]['word_level']])
                    else:
                        need_words.append(
                            [i, all_user_words[i]['word'], all_user_words[i]['word_ru'],
                             str(datetime.date.today()), 0])
            else:
                need_words.append(
                    [i, all_user_words[i]['word'], all_user_words[i]['word_ru'],
                     str(datetime.date.today()), 0])
        async with state.proxy() as data:
            data['ref3'] = need_words
    async with state.proxy() as data:
        need_words = data['ref3']
    if len(need_words) == 0:
        return False
    stupid = random.randint(0, len(need_words) - 1)
    i = 1
    array = []
    for k in words_in_use:
        array.append(k[0])
    while need_words[stupid][1] in array:
        stupid = random.randint(0, len(need_words) - 1)
        if i == len(need_words):
            return False
        i += 1
    return need_words[stupid]


@dp.callback_query_handler(text="training")
async def start_training(call: types.CallbackQuery, state: FSMContext):
    words_in_use = []
    async with state.proxy() as data:
        data['ref1'] = words_in_use
        data['ref5'] = call.from_user.id
    word = await get_random_word(call.from_user.username, state, flag=True)
    if not word:
        await call.message.answer('На сегодня слов не найдено')
    else:
        words_in_use.append([word[1]])
        await call.message.answer("Вы начали тренировку на день.\n"
                             "Вопрос №1. \n\n"
                             f"как переводится {word[1]}?")
        async with state.proxy() as data:
            data['ref1'] = words_in_use
        await Questions.Q1.set()


@dp.message_handler(state=Questions.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №2. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №3. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №4. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №4. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №6. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №7. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №8. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №9. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        words_in_use = data['ref1']
    words_in_use[-1].append(message.text)
    async with state.proxy() as data:
        data['ref1'] = words_in_use
    word = await get_random_word(message.from_user.username, state)
    if not word:
        await message.answer('На сегодня хватит')
        await state.reset_state(with_data=False)
        await change_dates(state)
    else:
        words_in_use.append([word[1]])
        await message.answer("Вопрос №10. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()
    async with state.proxy() as data:
        data['ref1'] = words_in_use


@dp.message_handler(state=Questions.Q10)
async def answer_q10(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ваши ответы!"
                         "Теперь проверим, были ли ошибки")
    await state.reset_state(with_data=False)
    await change_dates(state)
