from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from keyboards.courses_kb import courses_kb, course_info_kb
from keyboards.course_details_kb import course_detail_kb
from keyboards.success_kb import success_kb

router = Router()

@router.callback_query(F.data == "courses")
async def show_courses(callback: CallbackQuery):
    image = FSInputFile("media/images/course.png")
    caption = (
        "<b>Дополнительные курсы в школе Соробан</b>\n\n"
        "Соробан предлагает не только ментальную арифметику, но и другие развивающие курсы.\n\n"
        "Выберите понравившийся курс ниже, чтобы узнать подробности:"
    )
    await callback.message.answer_photo(photo=image, caption=caption, reply_markup=courses_kb)
    await callback.answer()


@router.callback_query(F.data == "course_programming")
async def show_programming_course(callback: CallbackQuery):
    image = FSInputFile("media/images/proger.png")

    caption = (
        "<b>🧑‍💻 НОВЫЙ КУРС ПО ПРОГРАММИРОВАНИЮ</b>\n\n"
        "🔸 Пробный урок бесплатно\n"
        "🔸 Обучение программированию, защите информационных систем, дизайну и компьютерной грамотности\n"
        "🔸 Возраст: от 12 лет\n"
        "🔸 Курс: 12 месяцев\n"
        "🔸 Длительность урока: 90 минут"
    )

    await callback.message.answer_photo(photo=image, caption=caption, reply_markup=course_info_kb)
    await callback.answer()


@router.callback_query(F.data == "course_speedcubing")
async def speedcubing_handler(callback: CallbackQuery):
    image = FSInputFile("media/images/cube.png")

    caption = (
        "<b>ТАКЖЕ СОРОБАН ПРЕДЛАГАЕТ СПИДКУБИНГ</b>\n\n"
        "🧩 <b>Как собрать кубик Рубика и развить интеллект?</b>\n"
        "О том, как головоломка, ещё и такая не современная, может развивать интеллектуальные способности, "
        "следует рассказать подробнее.\n\n"
        "📌 Вот, например, знали вы, что у детей спидкуберов формируется чёткая дикция, отличные навыки письма и "
        "способность быстро принимать решения? Секрет в том, что во время сборки кубика Рубика активно работают пальцы обеих рук, "
        "развивается мелкая моторика и активируются нейронные центры, ответственные за все перечисленные способности.\n\n"
        "🧠 Головоломка, способствующая раскрытию потенциала ребёнка и развитию его интеллекта.\n\n"
        "👦 Возраст: 7–99 лет\n"
        "📚 Курс: 8–10 занятий\n"
        "⏱️ Длительность урока: 60 минут\n" 
        "🧊 Кубик: 3×3"
    )

    await callback.message.answer_photo(photo=image, caption=caption, reply_markup=course_detail_kb)
    await callback.answer()


@router.callback_query(F.data == "back_to_courses")
async def back_to_courses(callback: CallbackQuery):
    await show_courses(callback)
