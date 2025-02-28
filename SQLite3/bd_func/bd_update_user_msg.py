# SQLite3/bd_func/bd_update_user_msg.py
# Обновление данных о сообщениях пользователя в базу данных bd|message

import sqlite3
from aiogram import types
from datetime import timezone, datetime, timedelta

from BotLibrary import types_message
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("update_user_messages",)


# Функция обновления статистики сообщений пользователя
async def update_user_messages(tg_id: int, message: types.Message, bd_name: str = BotVar.bd_names):
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
