# SQLite3/bd_func/status_user.py
# Проверка статусов пользователя с БД

import sqlite3
from aiogram import types
from ProjectsFiles import BotVar

# Функция проверки статуса пользователя
async def status_user(message: types.Message, bd_path: str = BotVar.bd_names):
    # Подключение к базе данных
    bd = sqlite3.connect(bd_path)
    tg_id = message.from_user.id
    cursor = bd.cursor()

    # Запрос к базе данных для получения значения из столбца 'user' для конкретного tg_id
    cursor.execute("SELECT user FROM users WHERE tg_id = ?", (tg_id,))

    # Получаем результат
    row = cursor.fetchone()

    # Словарь для сопоставления статусов
    status_map = {
        "ban": "Забаннен",
        "user": "Пользователь",
        "moderator": "Модератор",
        "admin": "Администратор",
        "so-owner": "Совладелец",
        "owner": "Владелец",
    }

    if row:
        user_type = row[0]  # предполагаем, что в столбце 'user' находится только одно значение
        status = status_map.get(user_type, "Ошибка!")  # Получаем статус или "Ошибка!"
    else:
        status = "Пользователь не найден"

    # Закрываем соединение с базой данных
    bd.close()

    # Выводим статус
    return status
