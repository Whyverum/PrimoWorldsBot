# BotCode/routers/utils/__init__.py
# Инициализация пакета utils, для работы с механиками

from aiogram import Router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="utils_head_router")

# Идет самым последним, если другие роутеры не сработали

