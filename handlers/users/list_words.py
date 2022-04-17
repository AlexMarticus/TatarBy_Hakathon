from aiogram import types

from api_control import getUsers, getUserWords
from loader import dp


@dp.message_handler(commands="list_words")
async def new_words_themes(message: types.Message):
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == message.from_user.username:
            user = i
            break
    all_user_words = await getUserWords(user)
    words = ''
    for i in all_user_words:
        words += f"""<i>{all_user_words[i]['word']} — {all_user_words[i]['word_ru']} </i>\n"""
    await message.answer(words)
