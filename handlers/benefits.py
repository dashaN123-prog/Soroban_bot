from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.utils.markdown import hbold
from keyboards.back_to_main import back_to_main_menu
from handlers.start import show_main_menu

router = Router()


@router.callback_query(F.data == "benefits")
async def show_benefits(callback: CallbackQuery):
    photo = FSInputFile("media/images/advantages_2.png")
    text = (
        f"{hbold('ПРЕИМУЩЕСТВА НАШЕЙ МЕТОДИКИ')}\n\n"
        f"{hbold('🧠 Уникальный онлайн тренажёр')}\n"
        "В нашем образовательном центре мы обучаемся\n"
        "на уникальном онлайн тренажере, который\n"
        "регулярно совершенствуется под растущие\n"
        "требования стандартов нашей методики.\n\n"

        f"{hbold('⏰ Тренируйтесь в любое удобное время')}\n"
        "Вам необходим лишь доступ в интернет и наличие\n"
        "любого электронного гаджета под рукой.\n"
        "Тренируйтесь максимально комфортно в любом\n"
        "месте: дома, на улице или в машине.\n\n"

        f"{hbold('👨‍👩‍👧 Обучайтесь вместе с ребёнком')}\n"
        "Наличие игровых форм в приложениях делает\n"
        "обучение увлекательным и любимым занятием не\n"
        "только для ребёнка, но и для его родителей."
    )
    await callback.message.answer_photo(photo=photo, caption=text, reply_markup=back_to_main_menu)
    await callback.answer()


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    await show_main_menu(callback.message)
    await callback.answer()
