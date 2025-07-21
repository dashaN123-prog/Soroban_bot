from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Ментальная арифметика", callback_data="about_arithmetic"),
        InlineKeyboardButton(text="📚 Курсы", callback_data="courses"),
    ],
    [
        InlineKeyboardButton(text="🎓 Успехи учеников", callback_data="success_1"),  # Начинаем с видео 1
        InlineKeyboardButton(text="💬 Отзывы", callback_data="reviews")
    ],
    [
        InlineKeyboardButton(text="🧠 Преимущества методики", callback_data="benefits"),
        InlineKeyboardButton(text="📸 Фотогалерея школы", callback_data="gallery")
    ],
    [
        InlineKeyboardButton(text="📝 Записаться", callback_data="register")
    ]
])
