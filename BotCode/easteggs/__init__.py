# BotCode/easteggs/__init__.py
# Инициализация модуля easteggs, для создания пасхалок

from aiogram import Router
from .holidays import router as holiday_router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="easteggs_router")


# Список подключаемых роутеров сверху-вниз
router.include_router(holiday_router)
