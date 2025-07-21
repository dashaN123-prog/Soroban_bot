from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

success_back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_start")]
])
