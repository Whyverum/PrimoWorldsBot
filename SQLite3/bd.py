import sqlite3
from aiogram import types
from datetime import datetime, timedelta, timezone

from BotLibrary import username as get_username, types_message
from ProjectsFiles import Permissions

bd_names: str = 'SQLite3/bd.db'

# Функция создания базы данных
async def create_user_db(bd_name: str = bd_names):
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,  -- Убрали AUTOINCREMENT
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

# Функция добавления пользователя с последовательным user_id
async def add_user(tg_id: int, username: str, first_name: str,
                   last_name: str, role: str, status: str, bd_name: str = bd_names):
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()

        # Проверяем, существует ли пользователь с таким tg_id
        cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
        if cursor.fetchone():
            return  # Пользователь уже существует, ничего не добавляем

        # Находим максимальный user_id
        cursor.execute("SELECT MAX(user_id) FROM users")
        max_id = cursor.fetchone()[0]
        new_user_id = 1 if max_id is None else max_id + 1

        # Добавляем нового пользователя
        cursor.execute('''
        INSERT INTO users (user_id, tg_id, username, first_name, last_name, role, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (new_user_id, tg_id, username, first_name, last_name, role, status))

        # Добавляем запись в user_messages
        cursor.execute('''
        INSERT INTO user_messages (user_id)
        VALUES (?)
        ''', (new_user_id,))

        db.commit()

# Функция обновления пользователя
async def update_user(tg_id: int, username: str = None, first_name: str = None, last_name: str = None,
                      bd_name: str = bd_names, role: str = None):
    updates = []
    params = []

    if username:
        updates.append("username = ?")
        params.append(username)
    if first_name:
        updates.append("first_name = ?")
        params.append(first_name)
    if last_name:
        updates.append("last_name = ?")
        params.append(last_name)
    if role:
        updates.append("role = ?")
        params.append(role)

    if updates:
        query = f"UPDATE users SET {', '.join(updates)} WHERE tg_id = ?"
        params.append(tg_id)
        with sqlite3.connect(bd_name) as db:
            cursor = db.cursor()
            cursor.execute(query, params)
            db.commit()

# Функция обновления статистики сообщений пользователя
async def update_user_messages(tg_id: int, message: types.Message, bd_name: str = bd_names):
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
        user_id = cursor.fetchone()
        if not user_id:
            return  # Пользователь не найден
        user_id = user_id[0]

        # Проверяем, существует ли запись в user_messages
        cursor.execute("SELECT last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages FROM user_messages WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()

        now = message.date.astimezone(timezone.utc)  # Время сообщения в UTC
        last_message = message.text or types_message(message)
        last_message_id = message.message_id

        if result:
            last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages = result
            if last_message_time:
                last_message_time = datetime.fromisoformat(last_message_time).astimezone(timezone.utc)
                # Сбрасываем статистику по времени
                if now - last_message_time >= timedelta(days=1):
                    messages_per_day = 0
                if now - last_message_time >= timedelta(weeks=1):
                    messages_per_week = 0
                if now - last_message_time >= timedelta(days=30):
                    messages_per_month = 0
            else:
                messages_per_day, messages_per_week, messages_per_month = 0, 0, 0

            # Увеличиваем счетчики
            messages_per_day += 1
            messages_per_week += 1
            messages_per_month += 1
            total_messages += 1
        else:
            # Если записи нет, создаем новую (хотя это уже должно быть сделано в add_user)
            messages_per_day, messages_per_week, messages_per_month, total_messages = 1, 1, 1, 1
            cursor.execute('INSERT INTO user_messages (user_id, last_message, last_message_id, last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                           (user_id, last_message, last_message_id, now.isoformat(), messages_per_day, messages_per_week, messages_per_month, total_messages))
            db.commit()
            return

        # Обновляем существующую запись
        cursor.execute('''
        UPDATE user_messages
        SET last_message = ?, last_message_id = ?, last_message_time = ?,
            messages_per_day = ?, messages_per_week = ?, messages_per_month = ?, 
            total_messages = ?
        WHERE user_id = ?
        ''', (last_message, last_message_id, now.isoformat(), messages_per_day,
              messages_per_week, messages_per_month, total_messages, user_id))
        db.commit()

# Основная обработка SQL
async def base_sql(message: types.Message):
    tg_id = message.from_user.id
    usernames = get_username(message)  # Изменено на get_username, чтобы избежать конфликта с переменной
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    if Permissions.sql_user:
        await add_user(tg_id, usernames, first_name, last_name, role="active", status="user")
        await update_user(tg_id=tg_id, first_name=first_name, last_name=last_name, status="user")
        await update_user_messages(tg_id, message)

# Функция для получения данных о пользователе
def get_user(tg_id: int, bd_name: str = bd_names):
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
        return cursor.fetchone()
