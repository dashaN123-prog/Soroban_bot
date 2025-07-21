import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def create_table():
    conn = await asyncpg.connect(DATABASE_URL)
    query = """
    CREATE TABLE IF NOT EXISTS registrations (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        course TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    );
    """
    await conn.execute(query)
    print("Таблица создана или уже существует.")
    await conn.close()

if __name__ == "__main__":
    asyncio.run(create_table())
