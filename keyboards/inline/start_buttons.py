from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


username_registration_inl_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Указать username", callback_data="indicate_username_in_site")
    ],
    [
        InlineKeyboardButton(text="Регистрация", callback_data="registration")
    ]
])
start_inl_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Мой список слов", callback_data="list_words"),
    ],
    [
        InlineKeyboardButton(text="Пройти тест", callback_data="test"),
        InlineKeyboardButton(text="Новые слова", callback_data="new_words")
    ]
])
