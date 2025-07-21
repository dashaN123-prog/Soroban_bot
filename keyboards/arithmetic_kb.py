from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

arithmetic_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_main"),
        InlineKeyboardButton(text="📝 Записаться", callback_data="register"),
    ]
])
