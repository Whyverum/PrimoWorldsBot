# BotLibrary/loggers/custom_loggers.py
# Кастомные логгеры для проекта, с более стандартизированным использованием

from loguru import logger
from ..validators import username
from aiogram.types import Message

# Настройка экспорта из модуля
__all__ = ("Logs",)


class Logs:
    """Класс для логирования с разными уровнями через loguru."""

    @staticmethod
    def debug(text: str = "Логирование!", log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне DEBUG.

        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(log_type=log_type, user=user).debug(text)

    @staticmethod
    def info(text: str = "Логирование!", log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне INFO.

        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(log_type=log_type, user=user).info(text)

    @staticmethod
    def warning(text: str = "Логирование!", log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне WARNING.

        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(log_type=log_type, user=user).warning(text)

    @staticmethod
    def error(text: str = "Логирование!", log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне ERROR.

        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(log_type=log_type, user=user).error(text)
