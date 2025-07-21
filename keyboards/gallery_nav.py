from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def gallery_nav_keyboard(index: int, total: int = 8) -> InlineKeyboardMarkup:
    buttons = []

    # Назад
    if index > 1:
        buttons.append(InlineKeyboardButton(text="◀️", callback_data=f"gallery_{index - 1}"))

    # Вперёд
    if index < total:
        buttons.append(InlineKeyboardButton(text="▶️", callback_data=f"gallery_{index + 1}"))

    # Общая разметка
    keyboard = [
        buttons,
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
