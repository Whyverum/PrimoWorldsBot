# SQLite3/bd_func/bd_update_user.py
# Обновление данных о пользователях в базу данных bd|user

import sqlite3
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("update_user",)


# Функция обновления пользователя
async def update_user(tg_id: int, username: str = None, first_name: str = None, last_name: str = None,
                      bd_name: str = BotVar.bd_names, role: str = None, user: str = None) -> None:
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
    if user:
        updates.append("user = ?")
        params.append(user)

    if updates:
        query = f"UPDATE users SET {', '.join(updates)} WHERE tg_id = ?"
        params.append(tg_id)
        with sqlite3.connect(bd_name) as db:
            cursor = db.cursor()
            cursor.execute(query, params)
            db.commit()
