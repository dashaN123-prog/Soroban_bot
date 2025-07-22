from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, InputMediaVideo

from keyboards.success_kb import get_success_kb
from handlers.start import show_main_menu

router = Router()

TOTAL_VIDEOS = 3

@router.callback_query(F.data.startswith("success_"))
async def success_pagination(callback: CallbackQuery):
    page_str = callback.data.split("_")[1]
    try:
        page = int(page_str)
    except ValueError:
        page = 1
    if page < 1 or page > TOTAL_VIDEOS:
        page = 1

    video_path = f"media/videos/success/video_{page}.mp4"
    video = FSInputFile(video_path)

    caption = "🎓 Посмотрите на успехи наших учеников!"

    media = InputMediaVideo(media=video, caption=caption)


    await callback.message.edit_media(media=media, reply_markup=get_success_kb(page, TOTAL_VIDEOS))
    await callback.answer()

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    await show_main_menu(callback.message)
    await callback.answer()
