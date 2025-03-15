# SQLite3/bd_func/bd_add_user.py
# Добавление пользователя в базу данных bd|user

import sqlite3
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("add_user",)


# Функция добавления пользователя с последовательным user_id
async def add_user(tg_id: int, username: str, first_name: str, last_name: str,
                   role: str, status: str, user: str, bd_name: str = BotVar.bd_names) -> None:
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
        INSERT INTO users (user_id, tg_id, username, first_name, last_name, role, status, user)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (new_user_id, tg_id, username, first_name, last_name, role, status, user))

        # Добавляем запись в user_messages
        cursor.execute('''
        INSERT INTO user_messages (user_id)
        VALUES (?)
        ''', (new_user_id,))

        db.commit()
