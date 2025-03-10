# database.py
import asyncpg
from config import DATABASE_URI

async def init_database():
    conn = await asyncpg.connect(DATABASE_URI)
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL
        );
    ''')
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            group_id BIGINT UNIQUE NOT NULL
        );
    ''')
    await conn.close()

async def add_user(user_id):
    conn = await asyncpg.connect(DATABASE_URI)
    await conn.execute('''
        INSERT INTO users (user_id)
        VALUES ($1)
        ON CONFLICT (user_id) DO NOTHING;
    ''', user_id)
    await conn.close()

async def add_group(group_id):
    conn = await asyncpg.connect(DATABASE_URI)
    await conn.execute('''
        INSERT INTO groups (group_id)
        VALUES ($1)
        ON CONFLICT (group_id) DO NOTHING;
    ''', group_id)
    await conn.close()

async def get_users():
    conn = await asyncpg.connect(DATABASE_URI)
    users = await conn.fetch('SELECT user_id FROM users;')
    await conn.close()
    return [user['user_id'] for user in users]

async def get_groups():
    conn = await asyncpg.connect(DATABASE_URI)
    groups = await conn.fetch('SELECT group_id FROM groups;')
    await conn.close()
    return [group['group_id'] for group in groups]

# Initialize the database when this module is imported
import asyncio
asyncio.get_event_loop().run_until_complete(init_database())
