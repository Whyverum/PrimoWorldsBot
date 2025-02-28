# SQLite3/bd_func/bd_get_user.py
# Получение информации о пользователе из базы данных bd|user

import sqlite3
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("get_user",)


# Функция для получения данных о пользователе
async def get_user(tg_id: int, bd_name: str = BotVar.bd_names):
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
        return cursor.fetchone()
