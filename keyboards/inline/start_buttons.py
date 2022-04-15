from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_username_registration_inl_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Готов", callback_data="start_work"),
    ],
    [
        InlineKeyboardButton(text="Указать username", callback_data="indicate_username_in_site")
    ],
    [
        InlineKeyboardButton(text="Регистрация", callback_data="registration")
    ]
])
