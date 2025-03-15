# BotCode/routers/common/messages.py
# Обработчик всех сообщений

from aiogram import Router, types
from BotLibrary import *
from SQLite3 import base_sql, status_user

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_msg_router")

# Обработчик всех сообщений
@router.message()
async def all_messages(message: types.Message) -> None:
    await base_sql(message)
    await status_user(message)
    Logs.msg(message)
