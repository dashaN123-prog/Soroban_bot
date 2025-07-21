from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
import os
from dotenv import load_dotenv
import asyncio

from handlers import start, courses, arithmetic, benefits, gallery, success
from registration import router as registration_router

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)
dp.include_router(courses.router)
dp.include_router(arithmetic.router)
dp.include_router(benefits.router)
dp.include_router(gallery.router)
dp.include_router(registration_router)
dp.include_router(success.router)


async def on_startup(bot: Bot):
    print("✅ Connected to bot")

async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
