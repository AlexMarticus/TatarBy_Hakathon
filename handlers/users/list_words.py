from aiogram import types

from api_control import getUsers, getUserWords
from loader import dp, bot


@dp.callback_query_handler(text="list_words")
async def new_words_themes(call: types.CallbackQuery):
    all_users = await getUsers()
    user = False
    for i in all_users:
        if all_users[i]["telegram_id"] == call.from_user.username:
            user = i
            break
    all_user_words = await getUserWords(user)
    words = ''
    for i in all_user_words:
        words += f"""<i>{all_user_words[i]['word']} — {all_user_words[i]['word_ru']} </i>\n"""
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, words)
