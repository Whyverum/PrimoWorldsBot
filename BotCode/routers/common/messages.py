# BotCode/routers/common/messages.py
# Обработчик всех сообщений

from aiogram import Router, types
from BotLibrary import *

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_msg_router")

# Обработчик всех сообщений
@router.message()
async def all_messages(message: types.Message) -> None:
    db.update_user(message)
    db.update_user_messages(message)
    Logs.msg(message)
