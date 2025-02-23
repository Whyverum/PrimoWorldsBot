# BotLibrary/system/logs.py
# Создание логгеров и их шаблон для проекта

import sys
from loguru import logger
from ProjectsFiles import BotLogs, ProjectPath


# Создание обычного логгера + логгер в файл
async def setup_logger() -> None:
    """
    Настройка логгеров для проекта, выводящих логи в консоль.
    Логгеры конфигурируются в зависимости от настроек в BotLogs.

    Если разрешено логирование, добавляются логи для уровней DEBUG, INFO, WARNING, ERROR.
    """
    logger.remove()  # Удаляем все логгеры

    if BotLogs.permission or BotLogs.permission_to_file:
        # Добавляем новый уровень START
        logger.level("START", no=25, color="white", icon="🔸")

    # Настройка логирования в консоль для каждого уровня
    if BotLogs.permission:
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
    if BotLogs.permission_to_file:
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
