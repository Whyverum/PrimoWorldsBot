# BotCode/routers/commands/user_cmd/stats_cmd.py
# Работа с командой /stats, для получения информации о себе
import sqlite3
from aiogram import types

from BotLibrary import CommandHandler, username_to_text, bot
from ProjectsFiles import BotVar

# Настройки экспорта в модули
__all__ = ("stats_cmd",)

# Функция получения информации о пользователи
async def send_stats(message: types.Message):
    with sqlite3.connect(BotVar.bd_names) as db:
        cursor = db.cursor()
        cursor.execute("SELECT messages_per_day, messages_per_week, messages_per_month, "
                       "total_messages FROM user_messages WHERE user_id = ?", (message.from_user.id,))
        stats = cursor.fetchone()
        if stats:
            await message.answer(f"Пользователь | {username_to_text(message)}\n"
                                 f"📊 Ваша статистика сообщений:\n"
                                 f"📅 За день: {stats[0]}\n"
                                 f"📆 За неделю: {stats[1]}\n"
                                 f"📅 За месяц: {stats[2]}\n"
                                 f"🔢 Всего: {stats[3]}")
        else:
            await message.answer("❌ Вы пока не отправили сообщений.")

# Создание команды /start с несколькими медиа
stats_cmd = CommandHandler(
    name="stats",
    description="Вывод статистики о пользователи",
    keywords=["stats", "ыефеы", "cnfnf", "стата", "Кто я", "Rnj z", "vjbcjj,otybz", "моисообщения"],
    callbackdata=["keywords"],
    media="command", func=[send_stats],
)
