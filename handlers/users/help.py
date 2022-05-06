from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from api_control import getUsers
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    all_users = await getUsers()
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            '/set_tat - Как установить татарскую раскладку')
    await message.answer("\n".join(text))
