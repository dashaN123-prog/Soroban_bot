import os
from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery, InlineKeyboardMarkup,
    InlineKeyboardButton, FSInputFile
)

router = Router()
VIDEO_FOLDER = "media/videos/success"

def get_video_list():
    return sorted([
        f for f in os.listdir(VIDEO_FOLDER)
        if f.lower().endswith((".mp4", ".mov", ".mkv"))
    ])

@router.callback_query(F.data == "success")
async def show_success_start(callback: CallbackQuery):
    video_files = get_video_list()
    if not video_files:
        await callback.message.answer("⚠️ Видео не найдены.")
        await callback.answer()
        return

    index = 0
    filepath = os.path.join(VIDEO_FOLDER, video_files[index])
    video = FSInputFile(filepath)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="▶️", callback_data=f"success:{index+1}")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])
    await callback.message.answer_video(video, caption="🎓 Успехи учеников", reply_markup=kb)
    await callback.message.delete()
    await callback.answer()

@router.callback_query(F.data.startswith("success:"))
async def paginate_success(callback: CallbackQuery):
    video_files = get_video_list()
    index = int(callback.data.split(":")[1])

    if index < 0 or index >= len(video_files):
        await callback.answer("📍 Это конец.")
        return

    filepath = os.path.join(VIDEO_FOLDER, video_files[index])
    video = FSInputFile(filepath)

    buttons = []
    if index > 0:
        buttons.append(InlineKeyboardButton(text="◀️", callback_data=f"success:{index-1}"))
    if index < len(video_files) - 1:
        buttons.append(InlineKeyboardButton(text="▶️", callback_data=f"success:{index+1}"))
    InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")


    kb = InlineKeyboardMarkup(inline_keyboard=[buttons])
    await callback.message.answer_video(video, caption="🎓 Успехи учеников", reply_markup=kb)
    await callback.message.delete()
    await callback.answer()
