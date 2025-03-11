# BotLibrary/timer/start_time.py
# Получение времени по разным часовым поясам

import pytz
from datetime import datetime
from tzlocal import get_localzone
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ProjectsFiles import BotVar

# Настройка экспорта из этого модуля
__all__ = ("scheduler", "get_city_time", "get_host_time")

# Создание планировщика для работы с задачами по времени
scheduler = AsyncIOScheduler(timezone=get_localzone().key)


# Функция получение иного времени
def get_city_time(city: str = 'Europe/Moscow') -> str:
    """
    Получение текущего времени по иному городскому времени.

    :param city: Город, что будет вторым временем
    :return: Строка, представляющая время в формате, заданном в BotVar.time_format.
    """
    # Устанавливаем временную зону для Москвы
    city_tz = pytz.timezone(city)
    # Возвращаем строку с форматом времени
    return datetime.now(city_tz).strftime(BotVar.time_format)


# Функция получение времени хоста
def get_host_time() -> str:
    """
    Получение текущего времени хоста (локального времени).

    :return: Строка, представляющая локальное время в формате, заданном в BotVar.time_format.
    """
    # Возвращаем строку с форматом времени
    return datetime.now().strftime(BotVar.time_format)
