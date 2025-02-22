# BotLibrary/system/logs.py
# Создание логгеров и их шаблон для проекта

import sys
from loguru import logger
from ProjectsFiles.configs.config import BotLogs

# Создание обычного логгера + логгер в файл
async def setup_logger():
    logger.remove()  # Удаляем все логгеры

    if BotLogs.permission:
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.info_text,
                   level="INFO",
                   filter=lambda record: record["level"].name == "INFO")
        logger.add(sys.stderr,
                   colorize=True,
                   format=BotLogs.error_text,
                   level="ERROR",
                   filter=lambda record: record["level"].name == "ERROR")

    if BotLogs.permission:
         """logger.add(ProjectPath.log_file,
                    rotation=BotLogs.max_size,
                    format=BotLogs.info_text,
                    backtrace=True,
                    diagnose=True,
                    level="INFO",
                    filter=lambda record: record["level"].name == "INFO")
         logger.add(ProjectPath.log_error_file,
                    rotation=BotLogs.max_size,
                    format=BotLogs.error_text,
                    backtrace=True,
                    diagnose=True,
                    level="ERROR",
                    filter=lambda record: record["level"].name == "ERROR")"""


# Создание функции логирования на обычные сообщения
async def common_msg_logginger(message,
                               name : str = "Пользователь",
                               message_type : str = "Медиа",
                               log_type : str = "Message"):
    if BotLogs.permission_msg:
        # Проверка на наличие текста и его типа
        if message.text is None:
            logger.bind(log_type=log_type, user=f"@{message.from_user.username}").info(
                f"Получено сообщение из ({name}) : {message_type}")
        else:
            logger.bind(log_type=log_type, user=f"@{message.from_user.username}").info(
                f"Получено сообщение из ({name}) : {message.text}")
