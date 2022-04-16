import asyncio
from contextlib import suppress

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from keyboards.inline.start_buttons import username_registration_inl_kb, start_inl_kb
from loader import dp
from api_control import prepare_url, getUsers, URL, changeUser, getUser


@dp.message_handler(commands="check")
async def how_to_set_tat_language(message: types.Message):
    print('@' + message.from_user.username)
    print(await getUsers())
    all_users = await getUsers()
    for i in all_users:
        print(i)
    print(await changeUser('1', 'Кирилл', '123', telegram_id="pro_stak666"))
    print(await changeUser('2', 'Антон', '333', telegram_id="seerb"))
    print(await getUser('2'))


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
Запомни, /training - твой главный помощник
""", reply_markup=start_inl_kb)


@dp.callback_query_handler(text='start_work')
async def start_work(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Ещё в разработке")
    await delete_message(call.message)


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
