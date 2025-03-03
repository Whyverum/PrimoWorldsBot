# BotCode/routers/common/messages.py
# Обработчик всех сообщений

from aiogram import Router, types
from BotLibrary import *
from SQLite3 import base_sql

# Настройка экспорта модулей и роутера
__all__ = ("router",)

from bd_func.status_user import status_user

router = Router(name="common_msg_router")


@router.message()
async def handle_all_messages(message: types.Message):
    await base_sql(message)
    await status_user(message)
    await logger_msg(message)  # Это твой метод для логирования
