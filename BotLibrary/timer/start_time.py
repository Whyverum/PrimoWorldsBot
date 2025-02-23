# BotLibrary/timer/start_time.py
# Получение времени по разным часовым поясам

import pytz
from datetime import datetime
from tzlocal import get_localzone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ProjectsFiles import BotVar

# Создание планировщика для работы с задачами по времени
scheduler = AsyncIOScheduler(timezone=get_localzone().key)


def get_moscow_time() -> str:
    """
    Получение текущего времени по московскому времени.

    :return: Строка, представляющая время в формате, заданном в BotVar.time_format.
    """
    # Устанавливаем временную зону для Москвы
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Получаем текущее время по московскому времени
    moscow_time = datetime.now(moscow_tz)
    # Возвращаем строку с форматом времени
    return moscow_time.strftime(BotVar.time_format)


def get_host_time() -> str:
    """
    Получение текущего времени хоста (локального времени).

    :return: Строка, представляющая локальное время в формате, заданном в BotVar.time_format.
    """
    # Получаем текущее время на хосте
    host_time = datetime.now()
    # Возвращаем строку с форматом времени
    return host_time.strftime(BotVar.time_format)
