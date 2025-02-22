# BotLibrary/timer/start_time.py
# Получение времени по

import pytz
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ProjectsFiles import BotVar

# Функция получение времени по Московскому времени
def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return moscow_time.strftime(BotVar.time_format)


# Функция получение времени хоста
def get_host_time():
    host_time = datetime.now()
    return host_time.strftime(BotVar.time_format)


# Создание планировщика
scheduler = AsyncIOScheduler(timezone=get_moscow_time())
