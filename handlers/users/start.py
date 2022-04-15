import asyncio
from contextlib import suppress

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from keyboards.inline.start_buttons import start_username_registration_inl_kb
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"""Привет, {message.from_user.full_name}!
У нас реализована экосистема сайт-telegram.
Если ты уже зарегистрирован на сайте и указал там 
свой username telegram'а, то жми "Готов".
Если ты не выполнил второе условие, то - "Указать username".
А если ты ещё не знаком с нами, "Регистрация" - то, что тебе нужно""", reply_markup=start_username_registration_inl_kb)


@dp.callback_query_handler(text='start_work')
async def start_work(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Ещё в разработке")
    await delete_message(call.message)


@dp.callback_query_handler(text='indicate_username_in_site')
async def indicate_username(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer(f"Перейдите на link, после входа в свой аккаунт, укажите telegram's username")
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
