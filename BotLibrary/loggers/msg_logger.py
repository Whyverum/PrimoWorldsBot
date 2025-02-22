# BotLibrary/loggers/msg_logger.py
# Логгер для всех не обработанных сообщений

from .logs import logger
from ProjectsFiles import BotLogs
from ..analytics.type_msg import types_message

# Настройка экспорта из модуля
__all__ = ("logger_msg",)

# Создание функции логирования на обычные сообщения
async def logger_msg(message, log_type : str = "Message"):
    user = f"@{message.from_user.username or message.from_user.id}"
    if BotLogs.permission:
        # Проверка на наличие текста и его типа
        if message.text is None:
            logger.bind(log_type=log_type, user=user).info(f"Получено сообщение из ({message.chat.id}) : {types_message(message)}")
        else:
            logger.bind(log_type=log_type, user=user).info(f"Получено сообщение из ({message.chat.id}) : {message.text}")
