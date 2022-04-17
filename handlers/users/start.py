import asyncio
from contextlib import suppress

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from api_control import getUsers
from keyboards.inline.start_buttons import username_registration_inl_kb
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    all_users = await getUsers()
    flag = False
    for i in all_users:
        if all_users[i]["telegram_id"] == message.from_user.username:
            flag = True
    if not flag:
        await message.answer(f"""Привет, {message.from_user.full_name}!
У нас реализована экосистема сайт-telegram.
Если ты не указал свой username telegram'а на сайте, то - "Указать username".
А если ты ещё не знаком с нами, "Регистрация" - то, что тебе нужно""", reply_markup=username_registration_inl_kb)
    else:
        await message.answer(f"""Привет, {message.from_user.full_name}!
/training - твой главный помощник(тренировка на день);
/list_words - увидеть свой список слов, которые находятся в программе изучения;
/new_words - узнать новые слова, распределённые оп темам;
/test - пройти тест на знание татарского
""")


@dp.callback_query_handler(text='indicate_username_in_site')
async def indicate_username(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Перейдите на link, после входа в свой аккаунт, укажите telegram'а username")
    await delete_message(call.message)


@dp.callback_query_handler(text='registration')
async def registration(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Перейдите на link и пройдите регистрацию")
    await delete_message(call.message)


async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()
