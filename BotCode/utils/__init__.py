# BotCode/routers/utils/__init__.py
# Инициализация пакета utils, для работы с механиками

from aiogram import Router
from .weather_api import get_weather

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", "get_weather")
router = Router(name="utils_head_router")

# Идет самым последним, если другие роутеры не сработали

