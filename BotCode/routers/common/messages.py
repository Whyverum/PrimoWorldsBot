# BotCode/routers/common/messages.py
# Обработчик всех сообщений

from aiogram import Router, types
from BotLibrary import *

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_msg_router")


# Хэндлер на все сообщения и записывает данные
@router.message()
async def handle_all_messages(message: types.Message):
    await logger_msg(message)
