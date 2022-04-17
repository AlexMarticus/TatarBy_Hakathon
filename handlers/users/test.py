from aiogram import types
from aiogram.dispatcher import FSMContext

from api_control import changeUser, getUsers, getUser
from loader import dp, bot
from states.test_lvl import Test


@dp.message_handler(commands="test")
async def start_test(message: types.Message, state: FSMContext):
    answers_all = []
    async with state.proxy() as data:
        data['ref10'] = answers_all
        data['ref11'] = message.from_user.username
    await message.answer("Вы начали тестирование. <strong>В ответ записывайте номер ответа.</strong>\n"
                         "Вопрос №1. \n\n"
                         "Гласные в татарском языке бывают мягкие и твёрдые.\n"
                         "В каком из слов буква «я» произносится в мягком варианте [йә]?\n\n"
                         "1 - яңгыр (дождь)\n"
                         "2 - ялкын (искра)\n"
                         "3 - ярдәм (помощь)\n"
                         "4 - кыяр (огурец)")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '4')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №2. \n\n"
                         "В каком из следующих слов все гласные относятся к типу твёрдых?\n\n"
                         "1 - үрдәк (утка)\n"
                         "2 - матур (красивый)\n"
                         "3 - зәңгәр (синий)\n"
                         "4 - әни (мама)")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №3. \n\n"
                         "На эту букву в татарском языке не начинается ни одно слово ?\n\n"
                         "1 - Ы\n"
                         "2 - Ю\n"
                         "3 - Ң\n"
                         "4 - Ө")
    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №4. \n\n"
                         "В каком из вариантов слово “лиса” написано правильно на татарском языке?\n\n"
                         "1 - телке\n"
                         "2 - төлке\n"
                         "3 - тэлке\n"
                         "4 - төлкө")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №5. \n\n"
                         "Какой знак препинания на татарском языке называют “өндәү билгесе?”\n\n"
                         "1 - точку\n"
                         "2 - точку с запятой\n"
                         "3 - вопросительный знак\n"
                         "4 - восклицательный знак")
    await Test.next()


@dp.message_handler(state=Test.Q5)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '4')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №6. \n\n"
                         "На календаре понедельник, или, с перевода на татарский язык:\n\n"
                         "1 - дүшәмбе\n"
                         "2 - пәнҗешәмбе\n"
                         "3 - җомга\n"
                         "4 - сишәмбе")
    await Test.next()


@dp.message_handler(state=Test.Q6)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №7. \n\n"
                         "Что Вам предложат, если вы загляниете в “китапханә” ?\n\n"
                         "1 - купить лекарство\n"
                         "2 - взять книгу\n"
                         "3 - купить билет\n"
                         "4 - посмотреть кино")
    await Test.next()


@dp.message_handler(state=Test.Q7)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №8. \n\n"
                         "2018 г. был объявлен годом Льва Толстого. Кем был Л. Толстой?\n\n"
                         "1 - җырчы\n"
                         "2 - шагыйрь\n"
                         "3 - язучы\n"
                         "4 - рәссам")
    await Test.next()


@dp.message_handler(state=Test.Q8)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №9. \n\n"
                         "Найдите слово, противоположное по значению «ача»\n\n"
                         "1 - килә\n"
                         "2 - чаба\n"
                         "3 - яба\n"
                         "4 - кайта")
    await Test.next()


@dp.message_handler(state=Test.Q9)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №10. \n\n"
                         "Подберите подходящее слово: Ул дару …\n\n"
                         "1 - уйлый\n"
                         "2 - тыңлый\n"
                         "3 - эчә\n"
                         "4 - укый")
    await Test.next()


@dp.message_handler(state=Test.Q10)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №11. \n\n"
                         "Найдите правильный перевод «Туган тел»\n\n"
                         "1 - татарский язык\n"
                         "2 - мой язык\n"
                         "3 - родной язык\n"
                         "4 - иностранный язык")
    await Test.next()


@dp.message_handler(state=Test.Q11)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №12. \n\n"
                         "Найдите неправильно написанное слово\n\n"
                         "1 - укутучы\n"
                         "2 - тәрәзә\n"
                         "3 - җәйге\n"
                         "4 - сөлге")
    await Test.next()


@dp.message_handler(state=Test.Q12)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №13. \n\n"
                         "Найдите слово из звонких согласных\n\n"
                         "1 - чиләк\n"
                         "2 - барабан\n"
                         "3 - ботка\n"
                         "4 - дәфтәр")
    await Test.next()


@dp.message_handler(state=Test.Q13)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №14. \n\n"
                         "Найдите противоположные слова\n\n"
                         "1 - эре – вак\n"
                         "2 - авыр – каты\n"
                         "3 - салкын – суык\n"
                         "4 - матур – чибәр")
    await Test.next()


@dp.message_handler(state=Test.Q14)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №15. \n\n"
                         "На какие вопросы отвечают глаголы настоящего времени?\n\n"
                         "1 - нишли?, нишлибез?\n"
                         "2 - нишләде?, нишләгән?\n"
                         "3 - нишләр?, нишләячәк?\n"
                         "4 - нишләсә? нишләмәсә?")
    await Test.next()


@dp.message_handler(state=Test.Q15)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №16. \n\n"
                         "Найдите мягкий гласный звук:\n\n"
                         "1 - а\n"
                         "2 - о\n"
                         "3 - ү\n"
                         "4 - ы")
    await Test.next()


@dp.message_handler(state=Test.Q16)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №17. \n\n"
                         "Найдите глаголы будущего времени\n\n"
                         "1 - көлде, бәйләгән\n"
                         "2 - күрәчәк, күрер\n"
                         "3 - килер, тапкан\n"
                         "4 - ашый, сөйләшә")
    await Test.next()


@dp.message_handler(state=Test.Q17)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №18. \n\n"
                         "Часть речи, которая обозначает предмет и отвечает на вопросы кто? что?\n\n"
                         "1 - исем\n"
                         "2 - фигыль\n"
                         "3 - сыйфат\n"
                         "4 - алмашлык")
    await Test.next()


@dp.message_handler(state=Test.Q18)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №19. \n\n"
                         "Найдите правильный перевод: “Гаилә бәйрәме”\n\n"
                         "1 - семейный друг\n"
                         "2 - семейный праздник\n"
                         "3 - школьный вечер\n"
                         "4 - национальный праздник")
    await Test.next()


@dp.message_handler(state=Test.Q19)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №20. \n\n"
                         "Какое слово написано правильно?\n\n"
                         "1 - өченче\n"
                         "2 - өчөнче\n"
                         "3 - өчөнчө\n"
                         "4 - өченчэ")
    await Test.next()


@dp.message_handler(state=Test.Q20)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №21. \n\n"
                         "Выберите слово с мягкими гласными\n\n"
                         "1 - дала\n"
                         "2 - җәнлек\n"
                         "3 - табигать\n"
                         "4 - болыт")
    await Test.next()


@dp.message_handler(state=Test.Q21)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №22. \n\n"
                         "Выберите правильное окончание: Без - табигать ... хуҗалары.\n\n"
                         "1 - нең\n"
                         "2 - ның\n"
                         "3 - тә\n"
                         "4 - не")
    await Test.next()


@dp.message_handler(state=Test.Q22)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №23. \n\n"
                         "Найдите правильный перевод к слову: янгын\n\n"
                         "1 - лес\n"
                         "2 - пожар\n"
                         "3 - природа\n"
                         "4 - родник")
    await Test.next()


@dp.message_handler(state=Test.Q23)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '2')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №24. \n\n"
                         "Продолжите предложение: Җәен дә, кышын да ...\n\n"
                         "1 - урманга йөрергә яратабыз\n"
                         "2 - дүртенче сыйныф укучысы\n"
                         "3 - урманда җиләк җыябыз\n"
                         "4 - файдалы үләннәр җыябыз")
    await Test.next()


@dp.message_handler(state=Test.Q24)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '1')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №25. \n\n"
                         "Найдите правильный перевод: Табигатьне саклагыз.\n\n"
                         "1 - лекарственные растения\n"
                         "2 - родной город\n"
                         "3 - берегите природу\n"
                         "4 - берегите лес")
    await Test.next()


@dp.message_handler(state=Test.Q25)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №26. \n\n"
                         "Найдите правильно построенное предложение\n\n"
                         "1 - Табигатьне зыян китермәгез\n"
                         "2 - Зыян китермәгез табигатькә\n"
                         "3 - Табигатькә зыян китермәгез\n"
                         "4 - Китермәгез зыян табигатьне")
    await Test.next()


@dp.message_handler(state=Test.Q26)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '3')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №27. \n\n"
                         "Выберите нужное слово: Укытучы безгә Татарстанның Кызыл китабы турында ...\n\n"
                         "1 - карады\n"
                         "2 - ашады\n"
                         "3 - барды\n"
                         "4 - сөйләде")
    await Test.next()


@dp.message_handler(state=Test.Q27)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
    answers_all.append(answer == '4')
    async with state.proxy() as data:
        data['ref10'] = answers_all
    await message.answer("Вопрос №28. \n\n"
                         "Выберите правильное окончание: Без - табигать.... яратабыз.\n\n"
                         "1 - нең\n"
                         "2 - ның\n"
                         "3 - тә\n"
                         "4 - не")
    await Test.next()


@dp.message_handler(state=Test.Q28)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        answers_all = data['ref10']
        user_id = data['ref11']
    id_shka = user_id
    answers_all.append(answer == '4')
    if sum(answers_all) / 28 < 0.33:
        await message.answer(f"Ваш уровень - Новичёк({sum(answers_all)} правильных ответов)")
        lvl = 1
    elif sum(answers_all) / 28 < 0.66:
        await message.answer(f"Ваш уровень - Средний({sum(answers_all)} правильных ответов)")
        lvl = 2
    else:
        await message.answer(f"Ваш уровень - Профи({sum(answers_all)} правильных ответов)")
        lvl = 3
    await state.finish()
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == id_shka:
            user = i
            break
    one_user = await getUser(user)
    await changeUser(user_id=user, name=one_user[user]['name'], email=one_user[user]['email'],
                     level_id=lvl)
