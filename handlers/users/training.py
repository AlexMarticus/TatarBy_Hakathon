from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import datetime
from loader import dp
from states.test import Questions
from api_control import prepare_url, getUsers, URL, changeUser, getUser, getUserWords, changeWord
import random
import datetime

words_is_in_use = []


async def get_random_word(user_id):
    global words_is_in_use
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == user_id:
            user = i
            break
    all_user_words = await getUserWords(user)
    need_words = []
    for i in all_user_words:
        if datetime.datetime.strptime(all_user_words[i]['date'].split(' ')[0], "%Y-%m-%d") == datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d") or all_user_words[i]['date'] is None:
            if datetime.datetime.strptime(all_user_words[i]['date'].split(' ')[0], "%Y-%m-%d") == datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d"):
                need_words.append(
                    [i, all_user_words[i]['word'], all_user_words[i]['word_ru'], all_user_words[i]['date'],
                     all_user_words[i]['word_level']])
            else:
                need_words.append(
                    [i, all_user_words[i]['word'], all_user_words[i]['word_ru'], datetime.date,
                     all_user_words[i]['word_level']])
    if len(need_words) == 0:
        return False
    stupid = random.randint(0, len(need_words) - 1)
    i = 1
    array = []
    for k in words_is_in_use:
        array.append(k[0])
    while need_words[stupid][1] in array:
        stupid = random.randint(0, len(need_words) - 1)
        i += 1
        if i == len(need_words):
            return False
    return need_words[stupid]


@dp.message_handler(commands="training")
async def start_training(message: types.Message):
    global words_is_in_use
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня слов не найдено')
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вы начали тренировку на день.\n"
                             "Вопрос №1. \n\n"
                             f"как переводится {word[1]}?")
        await Questions.Q1.set()


@dp.message_handler(state=Questions.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №2. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №3. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №4. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №4. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №6. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №7. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №8. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №9. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    global words_is_in_use
    words_is_in_use[-1].append(message.text)
    word = await get_random_word(message.from_user.username)
    if word == False:
        await message.answer('На сегодня хватит')
        await state.finish()
    else:
        words_is_in_use.append([word[1]])
        await message.answer("Вопрос №10. \n\n"
                             f"Как переводится {word[1]}?")
        await Questions.next()


@dp.message_handler(state=Questions.Q10)
async def answer_q10(message: types.Message, state: FSMContext):
    global words_is_in_use
    await message.answer("Спасибо за ваши ответы!"
                         "Теперь проверим, были ли ошибки")
    print(words_is_in_use)
    await state.finish()
