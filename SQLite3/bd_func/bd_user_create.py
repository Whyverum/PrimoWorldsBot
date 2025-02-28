# SQLite3/bd_func/bd_user_create.py
# Создание базы данных

import sqlite3
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("create_user_db",)

# Функция создания базы данных
async def create_user_db(bd_name: str = BotVar.bd_names):
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            tg_id INTEGER NOT NULL UNIQUE,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            role TEXT DEFAULT 'active',
            status TEXT DEFAULT 'user'
        );''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_messages (
            user_id INTEGER PRIMARY KEY,  -- Уникальный ключ
            last_message TEXT,
            last_message_id INTEGER,
            last_message_time TEXT,
            messages_per_day INTEGER DEFAULT 0,
            messages_per_week INTEGER DEFAULT 0,
            messages_per_month INTEGER DEFAULT 0,
            total_messages INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        );''')

        db.commit()
