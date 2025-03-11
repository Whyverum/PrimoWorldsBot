# BotLibrary/loggers/logs.py
# Создание логгеров и их шаблон для проекта

import sys
from loguru import logger
from ProjectsFiles import BotLogs, ProjectPath

# Настройка экспорта из модуля
__all__ = ("setup_logger",)

# Создание обычного логгера + логгер в файл
async def setup_logger(logging: bool = BotLogs.permission,
                       to_file: bool = BotLogs.permission_to_file) -> None:
    """
    Настройка логгеров для проекта, выводящих логи в консоль и файлы.
    Логгеры конфигурируются в зависимости от настроек в конфигах проекта.

    Если разрешено логирование, добавляются логи для уровней DEBUG, INFO, WARNING, ERROR.
    И кастомные такие, как START, NEW_USER, LEAVE_USER

    :param logging: Разрешение на логирование в консоль (config)
    :param to_file: Разрешение на логирование в файл (config)

    :return: Создание логеров под различные уровни
    """
    logger.remove()  # Удаляем все стандартные логгеры


    # Если есть разрешение, то он создает новые уровни
    if logging and BotLogs.permission_to_file:
        # Добавляем новый уровень START
        logger.level("START", no=25, color="white", icon="🔸")
    if logging and BotLogs.permission_new_user:
        # Добавляем новый уровень NEW_USER
        logger.level("NEW_USER", no=4, color="white", icon="👋")
    if logging and BotLogs.permission_leave_user:
        # Добавляем новый уровень LEAVE_USER
        logger.level("LEAVE_USER", no=3, color="white", icon="🫰")


    # Настройка логирования в консоль для каждого уровня
    if logging:
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.start_text,
                   level="START",
                   filter=lambda record: record["level"].name == "START"
        )
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.debug_text,
                   level="DEBUG",
                   filter=lambda record: record["level"].name == "DEBUG")
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.info_text,
                   level="INFO",
                   filter=lambda record: record["level"].name == "INFO")
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.warning_text,
                   level="WARNING",
                   filter=lambda record: record["level"].name == "WARNING")
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.error_text,
                   level="ERROR",
                   filter=lambda record: record["level"].name == "ERROR")


    # Добавление логгера для записи в файл
    if to_file:
        logger.add(ProjectPath.start_log_file,
                   rotation=BotLogs.max_size,
                   format=BotLogs.start_text,
                   backtrace=True,
                   diagnose=True,
                   level="START",
                   filter=lambda record: record["level"].name == "START")
        logger.add(ProjectPath.debug_log_file,
                   rotation=BotLogs.max_size,
                   format=BotLogs.debug_text,
                   backtrace=True,
                   diagnose=True,
                   level="DEBUG",
                   filter=lambda record: record["level"].name == "DEBUG")
        logger.add(ProjectPath.info_log_file,
                    rotation=BotLogs.max_size,
                    format=BotLogs.info_text,
                    backtrace=True,
                    diagnose=True,
                    level="INFO",
                    filter=lambda record: record["level"].name == "INFO")
        logger.add(ProjectPath.warning_log_file,
                    rotation=BotLogs.max_size,
                    format=BotLogs.warning_text,
                    backtrace=True,
                    diagnose=True,
                    level="WARNING",
                    filter=lambda record: record["level"].name == "WARNING")
        logger.add(ProjectPath.error_log_file,
                    rotation=BotLogs.max_size,
                    format=BotLogs.error_text,
                    backtrace=True,
                    diagnose=True,
                    level="ERROR",
                    filter=lambda record: record["level"].name == "ERROR")
