import asyncio
from contextlib import suppress
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InputFile
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from keyboards.inline.oc_buttons import operation_sys
from loader import dp, bot


@dp.message_handler(commands="set_tat")
async def how_to_set_tat_language(message: types.Message):
    await message.answer('Выберите Вашу операционную систему', reply_markup=operation_sys)


@dp.callback_query_handler(text='ios_set_lang')
async def ios_set_lang(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Для этого скачайте Gboard (клавиатура для телефона от Google),"
                              "при установке укажите татарский язык. В настройках телефона установите"
                              "клавиатуру Gboard по умолчанию. Готово!")
    await delete_message(call.message)


@dp.callback_query_handler(text='mac_set_lang')
async def mac_set_lang(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.reply_document(open('tatar_keyboard.dmg', 'rb'))
    await call.message.answer("""Раскладка клавиатуры позволяет использовать привычный способ набора татарских символов в устройствах под управлением macOS:
— для набора татарских букв: ө-ц, һ-§ (кнопка левее «1»), ә-щ, ү-ъ, ң-ж, җ-ь;
— для набора букв ц, щ, ъ, ь, ж — необходимо вводить их с зажатой клавишей alt;
— для ввода точки используется клавиша «/», справа от «ю»; для ввода запятой — shift + «/».

1. Скачайте документ;
2. Откройте сохраненный файл, в открывшемся окне перенесите файлы Tatar и Tatar.icns в указанную папку;
3. Перезагрузите устройство;
4. В Настройках (System Preferences) откройте раздел клавиатуры (Keyboard) — Источники ввода (Input Sources), нажмите на кнопку +, в списке слева выберите Другие (Others), после чего справа выберите Tatar и нажмите кнопку Добавить (Add).
5. Клавиатура добавлена в список выбранных Вами раскладок и может быть использована.""")


@dp.callback_query_handler(text='android_set_lang')
async def android_set_lang(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Для этого скачайте Gboard (клавиатура для телефона от Google),"
                              "при установке укажите татарский язык. В настройках телефона установите"
                              "клавиатуру Gboard по умолчанию. Готово!")
    await delete_message(call.message)


@dp.callback_query_handler(text='windows_set_lang')
async def windows_set_lang(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("""Для этого кликаем правой кнопкой мышки на «Языковую панель» («RU»), 
которая расположена в правом нижнем углу экрана. Выбираем пункт «Параметры» 
и переходим в окно «Языки и службы текстового ввода». Теперь остаётся только выбрать и добавить язык!
Расположение татарских букв (кириллица) основано на русской клавиатуре. Когда вы будете набирать текст на 
татарском языке, вам придётся нажимать клавиши, которые используются сравнительно редко. 
По решению Microsoft татарские буквы расположены так, как показано ниже:

Буква Ә на клавише Щ;
Буква Ө на клавише Ц;
Буква Ү на клавише Ъ; 
Буква Җ на клавише Ь; 
Буква Ң на клавише Ж;
Буква Һ на клавише Ё.

Если в тексте вам нужно использовать эти русские буквы, не нужно менять раскладку: их следует писать,
нажимая одновременно с клавишами «Ctrl» и «Alt». Например, чтобы набрать букву «ж», нажмите одновременно «Ctrl+Alt+ж».""")
    await delete_message(call.message)


async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()
