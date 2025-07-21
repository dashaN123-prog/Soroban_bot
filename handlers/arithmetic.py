from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.arithmetic_kb import arithmetic_kb


router = Router()

@router.callback_query(F.data == "about_arithmetic")
async def about_arithmetic_handler(callback: CallbackQuery):
    video = FSInputFile("media/videos/arithmetic.mp4")

    caption = (
        "🧠 <b>Что такое ментальная арифметика?</b>\n"
        "Программа в школе устного счёта Соробан для детей от 5 до 12 лет.\n\n"
        "Это программа развития интеллектуальных способностей у детей. "
        "Устный счёт — это самый лучший тренажёр для мозга. "
        "В основе занятий лежит развитие левого и правого полушария мозга. "
        "Именно от гармоничного развития обоих полушарий зависит то, "
        "насколько успешным будет ваш ребёнок."
    )

    await callback.message.answer_video(
        video=video,
        caption=caption,
        reply_markup=arithmetic_kb
    )

    await callback.answer()

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    text = (
        "✨ <b>Ментальная арифметика</b> — это способ развития интеллекта детей через устный счёт. "
        "Гармоничное развитие обоих полушарий мозга помогает ребёнку легче учиться и мыслить быстрее.\n\n"
        "📌 <b>Как проходят занятия в Соробан?</b>\n"
        "▫️ 8–10 академических часов в месяц\n"
        "▫️ Занятия проходят в игровой форме\n"
        "▫️ В группе до 6 человек\n"
        "▫️ Ежедневные домашние тренировки в онлайн-режиме\n\n"
        "👇 <b>Выберите интересующий раздел:</b>"
    )
    from keyboards.main_menu import main_menu
    await callback.message.answer(text, reply_markup=main_menu)
    await callback.answer()

