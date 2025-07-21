from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from keyboards.main_menu import main_menu

router = Router()

async def show_main_menu(target):
    photo = FSInputFile("media/images/description.png")
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
    await target.answer_photo(photo=photo, caption=text, reply_markup=main_menu)

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await show_main_menu(message)

@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    await show_main_menu(callback.message)
    await callback.answer()
