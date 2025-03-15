# SQLite3/bd_func/bd_update_user_msg.py
# Обновление данных о сообщениях пользователя в базу данных bd|message

import sqlite3
from aiogram import types
from datetime import timezone, datetime, timedelta

from BotLibrary import type_msg
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("update_user_messages",)


# Функция обновления статистики сообщений пользователя
async def update_user_messages(message: types.Message, bd_name: str = BotVar.bd_names) -> None:
    with sqlite3.connect(bd_name) as db:
        cursor = db.cursor()
        user_id = message.from_user.id  # Используем user_id напрямую

        # Проверяем, существует ли запись в user_messages
        cursor.execute(
            "SELECT last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages FROM user_messages WHERE user_id = ?",
            (user_id,))
        result = cursor.fetchone()

        # Время сообщения в московском времени
        now = message.date.astimezone(timezone(timedelta(hours=3)))
        today = now.date()
        start_of_week = today - timedelta(days=today.weekday())  # Понедельник текущей недели
        current_month = now.month
        current_year = now.year

        last_message = message.text or type_msg(message)
        last_message_id = message.message_id

        if result:
            last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages = result
            if last_message_time:
                last_message_time = datetime.fromisoformat(last_message_time).astimezone(timezone(timedelta(hours=3)))
                last_date = last_message_time.date()
                last_week = last_date - timedelta(days=last_date.weekday())
                last_month = last_message_time.month
                last_year = last_message_time.year

                # Обнуляем счетчики, если наступил новый день, неделя или месяц
                if last_date != today:
                    messages_per_day = 0
                if last_week != start_of_week:
                    messages_per_week = 0
                if last_month != current_month or last_year != current_year:
                    messages_per_month = 0
            else:
                messages_per_day, messages_per_week, messages_per_month = 0, 0, 0

            # Увеличиваем счетчики
            messages_per_day += 1
            messages_per_week += 1
            messages_per_month += 1
            total_messages += 1
        else:
            # Если записи нет, создаем новую
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
