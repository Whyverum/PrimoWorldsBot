# BotLibrary/loggers/msg_logger.py
# Логгер для всех не обработанных сообщений

from ProjectsFiles import BotLogs
from .custom_loggers import Logs
from ..analytics.type_msg import types_message
from aiogram.types import Message

# Настройка экспорта из модуля
__all__ = ("logger_msg",)

# Создание функции логирования на обычные сообщения
async def logger_msg(message: Message, log_type: str = "Message") -> None:
    """
    Логирует сообщение, если оно не обработано.

    :param message: Сообщение от пользователя.
    :param log_type: Тип лога (по умолчанию "Message").
    """
    # Получаем username или id пользователя
    user: str = f"@{message.from_user.username or message.from_user.id}"
    msg_type = types_message(message)

    # Логирование только если разрешено
    if BotLogs.permission:
        # Проверка на наличие текста и его типа
        if message.text is None and msg_type not in ("Новые участники чата", "Ушедший участник чата"):
            Logs.info(log_type=log_type, user=user, text=f"Получено сообщение из ({message.chat.id}) : {msg_type}")
        elif message.text is not None:
            Logs.info(log_type=log_type, user=user, text=f"Получено сообщение из ({message.chat.id}) : {message.text}")
        else:
            return
