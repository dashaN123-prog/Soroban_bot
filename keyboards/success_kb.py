from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_success_kb(current_page: int, total: int):
    prev_page = current_page - 1 if current_page > 1 else total
    next_page = current_page + 1 if current_page < total else 1

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️", callback_data=f"success_{prev_page}"),
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main"),
            InlineKeyboardButton(text="➡️", callback_data=f"success_{next_page}"),
        ]
    ])
    return keyboard
