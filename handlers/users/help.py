from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from api_control import getUsers
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    all_users = await getUsers()
    flag = False
    for i in all_users:
        if all_users[i]["telegram_id"] == message.from_user.username:
            flag = True
    if not flag:
        text = ("Список команд: ",
                "/start - Начать диалог",
                "/help - Получить справку",
                '/set_tat - Как установить татарскую раскладку')
    else:
        text = ("Список команд: ",
                "/start - Начать диалог",
                "/help - Получить справку",
                '/set_tat - Как установить татарскую раскладку',
                '/training - Начать дневную трениовку',
                '/new_words - узнать новые слова, распределённые по темам',
                '/list_words - получить список всех изучаемых слов')
    await message.answer("\n".join(text))
