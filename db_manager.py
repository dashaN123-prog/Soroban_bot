import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

async def get_connection():
    return await asyncpg.connect(DATABASE_URL)

async def add_registration(name: str, phone: str, course: str):
    conn = await get_connection()
    await conn.execute(
        "INSERT INTO registrations (name, phone, course) VALUES ($1, $2, $3)",
        name, phone, course
    )
    await conn.close()

async def get_all_registrations():
    conn = await get_connection()
    rows = await conn.fetch("SELECT id, name, phone, course, created_at FROM registrations ORDER BY created_at DESC")
    await conn.close()
    return rows

async def delete_registration(reg_id: int):
    conn = await get_connection()
    await conn.execute("DELETE FROM registrations WHERE id = $1", reg_id)
    await conn.close()
