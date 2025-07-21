import os
from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import (
    Message, CallbackQuery,
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db_manager import add_registration, get_all_registrations, delete_registration

load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN_ID"))

router = Router()

# Шаги регистрации
class RegistrationForm(StatesGroup):
    name = State()
    phone = State()
    course = State()

@router.callback_query(F.data == "register")
async def start_register(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("✏️ Введите имя ребёнка:")
    await state.set_state(RegistrationForm.name)

@router.message(RegistrationForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📱 Введите номер телефона:")
    await state.set_state(RegistrationForm.phone)

@router.message(RegistrationForm.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Ментальная арифметика")],
        [KeyboardButton(text="Программирование")],
        [KeyboardButton(text="Спидкубинг")]
    ], resize_keyboard=True)

    await message.answer("📚 Выберите курс:", reply_markup=kb)
    await state.set_state(RegistrationForm.course)

@router.message(RegistrationForm.course)
async def get_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    data = await state.get_data()

    await add_registration(data["name"], data["phone"], data["course"])

    await message.answer(
        "✅ Спасибо за запись! Мы свяжемся с вами в ближайшее время.",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()

# Просмотр записей (только для админа)
@router.message(F.text == "/show")
async def show_registrations(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ У вас нет доступа к этой команде.")
        return

    registrations = await get_all_registrations()

    if not registrations:
        await message.answer("Пока нет записей.")
        return

    for reg in registrations:
        text = (
            f"👤 {reg['name']}\n"
            f"📱 {reg['phone']}\n"
            f"📚 {reg['course']}\n"
            f"🕒 {reg['created_at'].strftime('%d.%m.%Y %H:%M')}\n"
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Удалить", callback_data=f"delete:{reg['id']}")]
        ])
        await message.answer(text, reply_markup=kb)

# Хендлер удаления записи по кнопке
@router.callback_query(F.data.startswith("delete:"))
async def delete_registration_handler(callback: CallbackQuery):
    reg_id = int(callback.data.split(":")[1])
    await delete_registration(reg_id)
    await callback.message.edit_text("✅ Запись удалена.")
    await callback.answer()
