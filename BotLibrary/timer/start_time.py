# BotLibrary/timer/start_time.py
# Получение времени по разным часовым поясам

from datetime import datetime
from tzlocal import get_localzone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ProjectsFiles import BotVar

# Настройка экспорта из этого модуля
__all__ = ("scheduler", "get_city_time", "get_host_time")

# Создание планировщика для работы с задачами по времени
scheduler = AsyncIOScheduler(timezone=get_localzone().key)


def get_city_time(city: str = 'Europe/Moscow',
                  time_format: str = BotVar.time_format) -> str:
    """
    Получение текущего времени по иному городскому времени.

    :param city: Город, что будет вторым временем.
    :param time_format: Шаблон форматирования времени (конфиг).
    :return: Строка, представляющая время в формате, заданном в BotVar.time_format.
    """
    from pytz import timezone
    # Устанавливаем временную зону для Москвы
    city_tz = timezone(city)
    # Возвращаем строку с форматом времени
    return datetime.now(city_tz).strftime(time_format)


def get_host_time(time_format: str = BotVar.time_format) -> str:
    """
    Получение текущего времени хоста (локального времени).

    :param time_format: Шаблон форматирования времени (конфиг).
    :return: Строка, представляющая локальное время в формате format.
    """
    # Возвращаем строку с форматом времени
    return datetime.now().strftime(time_format)
