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
    def start(text: str = "Логирование!", system: str = "PRIMO",
              log_type: str = "AEP", user: str = "@Console") -> None:
        """
        Логирует сообщение на уровне DEBUG.

        :param system:
        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        """
        logger.bind(system=system, user=user, log_type=log_type).log("START", text)

    @staticmethod
    def debug(text: str = "Логирование!", system : str = "DEBUG",
              log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне DEBUG.

        :param system:
        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).debug(text)

    @staticmethod
    def info(text: str = "Логирование!", system : str = "PRIMO",
             log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне INFO.

        :param system:
        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).info(text)

    @staticmethod
    def warning(text: str = "Логирование!", system : str = "WARNING",
                log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне WARNING.

        :param system:
        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).warning(text)

    @staticmethod
    def error(text: str = "Логирование!", system : str = "ERROR",
              log_type: str = "Logs", user: str = "@Console", message: Message = None) -> None:
        """
        Логирует сообщение на уровне ERROR.

        :param system:
        :param text: Сообщение для логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).error(text)
