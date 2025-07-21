from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

course_detail_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_courses"),
        InlineKeyboardButton(text="📝 Записаться", callback_data="register")
    ]
])
