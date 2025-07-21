from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

courses_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_start"),  # ← здесь changed
    ],
    [
        InlineKeyboardButton(text="💻 Программирование", callback_data="course_programming"),
        InlineKeyboardButton(text="🧩 Спидкубинг", callback_data="course_speedcubing")
    ]
])

course_info_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_courses"),  # ← оставь как есть
        InlineKeyboardButton(text="📝 Записаться", callback_data="register")
    ]
])
