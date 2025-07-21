from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.gallery_nav import gallery_nav_keyboard
from aiogram.types import InputMediaPhoto

router = Router()

@router.callback_query(F.data == "gallery")
async def show_first_gallery(callback: CallbackQuery):
    await send_gallery_photo(callback, index=1)
    await callback.answer()


@router.callback_query(F.data.startswith("gallery_"))
async def handle_gallery_navigation(callback: CallbackQuery):
    index = int(callback.data.split("_")[1])
    await send_gallery_photo(callback, index)
    await callback.answer()


async def send_gallery_photo(callback: CallbackQuery, index: int):
    photo_path = f"media/gallery/photo{index}.png"
    photo = FSInputFile(photo_path)

    caption = (
        "📷 <b>ФОТОГАЛЕРЕЯ ШКОЛЫ СОРОБАН</b>\n\n"
        f" Фото {index} из 8"
    )

    media = InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML")

    try:

        await callback.message.edit_media(
            media=media,
            reply_markup=gallery_nav_keyboard(index)
        )
    except Exception:


        await callback.message.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=gallery_nav_keyboard(index),
            parse_mode="HTML"
        )
        try:
            await callback.message.delete()
        except:
            pass
