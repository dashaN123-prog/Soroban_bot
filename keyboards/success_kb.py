from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_success_kb(page: int, total_pages: int = 3) -> InlineKeyboardMarkup:
    prev_page = page - 1 if page > 1 else total_pages
    next_page = page + 1 if page < total_pages else 1

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️", callback_data=f"success_{prev_page}"),
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_start"),
            InlineKeyboardButton(text="▶️", callback_data=f"success_{next_page}"),
        ]
    ])
    return kb
