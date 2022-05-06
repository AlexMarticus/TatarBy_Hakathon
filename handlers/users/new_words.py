import datetime
import random

from aiogram import types
from aiogram.types import CallbackQuery

from api_control import getUsers, getWords, appendWord, getUserWords, createWord, changeWordLevel
from keyboards.inline.new_words_buttons import themes_for_new_words
from loader import dp, bot
from utils.translate import rus_to_tat_translate


@dp.callback_query_handler(text="new_words")
async def new_words_themes(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    text = 'Выберите тему, слово которой Вы желаете заучить'
    await bot.send_message(call.from_user.id, text, reply_markup=themes_for_new_words)


@dp.callback_query_handler(text='whether_kb')
async def whether_f(call: CallbackQuery):
    weather = ["погода", "прекрасный", "ужасный", "холодный", "жаркий", "теплый", "небо", "солнце", "дождь", "ветер",
               "облако",
               "снег", "солнечный", "дождливый", "ветреный", "облачный", "яркий", "снежный", "идет", "дождь", "идет",
               "снег",
               "дуть", "светить", "теплее", "становиться", "холоднее", "измениться"]
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == call.from_user.username:
            user = i
            break
    word_ids = all_users[user]['words']
    rus_word = random.choice(weather)
    tat_word = rus_to_tat_translate(rus_word)
    words_of_user = await getUserWords(user)
    flag = True
    for i in words_of_user:
        if words_of_user[i]['word'] == tat_word:
            flag = False
    while tat_word is None and flag:
        rus_word = random.choice(weather)
        tat_word = rus_to_tat_translate(rus_word)
        flag = True
        for i in words_of_user:
            if words_of_user[i]['word'] == tat_word:
                flag = False
    await call.message.answer(f'Добавили новое слово в программу для обучения:\n\n{tat_word} - {rus_word}')
    all_words = await getWords()
    word_id = 1234567890
    for i in all_words:
        if all_words[i]['word_ru'] == rus_word:
            word_id = i
            break
    await appendWord(user, word_id)


@dp.callback_query_handler(text='family_kb')
async def family_f(call: CallbackQuery):
    family = ["отец", "мать", "родители", "сын", "дочь", "сестра", "брат", "двоюродный брат", "родной брат",
              "троюродный "
              "брат",
              "сестра", "близнецы", "тетя", "дядя", "племянник", "племянница", "дедушка", "бабушка",
              "дедушка и бабушка",
              "прабабушка", "прадедушка", "внук", "внучка", "муж", "жена", "ребенок", "дети", "внуки", "малыш",
              "родственник"]
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == call.from_user.username:
            user = i
            break
    rus_word = random.choice(family)
    tat_word = rus_to_tat_translate(rus_word)
    words_of_user = await getUserWords(user)
    flag = True
    for i in words_of_user:
        if words_of_user[i]['word'] == tat_word:
            flag = False
    while tat_word is None and not flag:
        rus_word = random.choice(family)
        tat_word = rus_to_tat_translate(rus_word)
        flag = True
        for i in words_of_user:
            if words_of_user[i]['word'] == tat_word:
                flag = False
    await call.message.answer(f'Добавили новое слово в программу для обучения:\n\n{tat_word} - {rus_word}')
    await createWord(tat_word, rus_word)
    all_words = await getWords()
    word_id = max(list(map(int, all_words.keys())))
    print(word_id)
    await appendWord(user, word_id)
    await changeWordLevel(user, word_id, 0, str(datetime.datetime.now()))
    print(await getWords())


@dp.callback_query_handler(text='travelling_kb')
async def travelling_f(call: CallbackQuery):
    travelling = ["поездка в", "по всему миру", "ехать в", "добраться до", "путешествовать в", "посетить разные страны",
                  "музеи и галереи", "осматривать достопримечательности", "увидеть достопримечательности",
                  "путешествовать "
                  "(ехать) за "
                  "границу",
                  "путешествовать (ехать) по …", "путешествовать (ехать) на машине (автобусе)",
                  "путешествовать (ехать) на поезде", "путешествовать (ехать) на самолете",
                  "путешествовать (ехать) морем",
                  "уехать из", "провести неделю в…", "по дороге; НО on the way home", "во время поездки",
                  "остановиться в отеле", "гулять по городу", "пробовать местную пищу", "покупать сувениры",
                  "увлекательный", "необычный", "знакомиться с новыми людьми", "улучшить свой английский",
                  "загорать на пляже", "замечательно провести время", "получить удовольствие от поездки",
                  "вернуться домой"]
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == call.from_user.username:
            user = i
            break
    rus_word = random.choice(travelling)
    tat_word = rus_to_tat_translate(rus_word)
    words_of_user = await getUserWords(user)
    flag = True
    for i in words_of_user:
        if words_of_user[i]['word'] == tat_word:
            flag = False
    while tat_word is None and flag:
        rus_word = random.choice(travelling)
        tat_word = rus_to_tat_translate(rus_word)
        flag = True
        for i in words_of_user:
            if words_of_user[i]['word'] == tat_word:
                flag = False
    await call.message.answer(f'Добавили новое слово в программу для обучения:\n\n{tat_word} - {rus_word}')
    all_words = await getWords()
    word_id = 1234567890
    for i in all_words:
        if all_words[i]['word_ru'] == rus_word:
            word_id = i
            break
    await appendWord(user, word_id)


@dp.callback_query_handler(text='food_kb')
async def food_f(call: CallbackQuery):
    food = ["бутерброд", "поджаренный хлеб", "торт, пирожное", "булочка", "чай", "кофе", "сахар", "каша", "сыр",
            "колбаса",
            "сосиски", "соль", "перец", "салат", "суп", "мясо", "курица", "рыба", "котлеты", "картошка", "помидоры",
            "овощи", "суп", "хлеб", "масло", "напиток", "молоко", "сок", "кока-кола", "минеральная вода", "мороженое",
            "фрукты", " завтрак", " обед", "ужин", "выпить кофе вместо чая", "испытывать голод", "испытывать жажду",
            "пить",
            "есть", "готовить", "налить чашечку чая", "мыть посуду", "мыть руки перед едой", " быть готовым",
            "закончен"]
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == call.from_user.username:
            user = i
            break
    rus_word = random.choice(food)
    tat_word = rus_to_tat_translate(rus_word)
    words_of_user = await getUserWords(user)
    flag = True
    for i in words_of_user:
        if words_of_user[i]['word'] == tat_word:
            flag = False
    while tat_word is None and flag:
        rus_word = random.choice(food)
        tat_word = rus_to_tat_translate(rus_word)
        flag = True
        for i in words_of_user:
            if words_of_user[i]['word'] == tat_word:
                flag = False
    await call.message.answer(f'Добавили новое слово в программу для обучения:\n\n{tat_word} - {rus_word}')
    all_words = await getWords()
    word_id = 1234567890
    for i in all_words:
        if all_words[i]['word_ru'] == rus_word:
            word_id = i
            break
    await appendWord(user, word_id)
