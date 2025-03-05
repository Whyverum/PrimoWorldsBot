# BotCode/routers/utils/__init__.py
# Инициализация пакета utils, для работы с механиками

from aiogram import Router
from .admin_list import admin_lists
from .all_admins_hide import hidden_admins_message
from .weather_api import get_weather

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", "get_weather", "admin_lists", "hidden_admins_message")
router = Router(name="utils_head_router")

# Идет самым последним, если другие роутеры не сработали

