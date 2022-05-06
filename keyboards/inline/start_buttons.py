from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


username_registration_inl_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Указать username", callback_data="indicate_username_in_site")
    ],
    [
        InlineKeyboardButton(text="Регистрация", callback_data="registration")
    ]
])
main_bts_in_start = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Тренировка на день", callback_data="training"),
        InlineKeyboardButton(text="Список изучаемых слов", callback_data="list_words")
    ],
    [
        # InlineKeyboardButton(text="Выучить новые слова", callback_data="new_words"),
        InlineKeyboardButton(text="Пройти тест на знание татарского", callback_data="test")
    ]
])
