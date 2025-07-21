from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from keyboards.success_kb import get_success_kb
from handlers.start import show_main_menu  # Импорт функции главного меню

router = Router()

TOTAL_VIDEOS = 3  # количество видео

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

    caption = f"🎓 Посмотрите на успехи наших учеников!"

    try:
        await callback.message.delete()
    except:
        pass

    await callback.message.answer_video(
        video=video,
        caption=caption,
        reply_markup=get_success_kb(page, TOTAL_VIDEOS)
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_start")
async def back_to_start(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    await show_main_menu(callback.message)
    await callback.answer()
