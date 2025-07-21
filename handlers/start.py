from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
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
    if isinstance(target, CallbackQuery):
        await target.message.edit_media(
            media=InputMediaPhoto(media=photo, caption=text, parse_mode="HTML"),
            reply_markup=main_menu
        )
    else:
        await target.answer_photo(photo=photo, caption=text, reply_markup=main_menu)


@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await show_main_menu(message)


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await show_main_menu(callback)
    await callback.answer()
