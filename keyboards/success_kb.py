from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

success_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎓 Успехи учеников", callback_data="show_success")]
])