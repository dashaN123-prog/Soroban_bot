import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def connect_db():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        print("✅ Подключение успешно!")
        await conn.close()
    except Exception as e:
        print("❌ Ошибка подключения:", e)

if __name__ == "__main__":
    import asyncio
    asyncio.run(connect_db())
