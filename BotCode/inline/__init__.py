# BotCode/inline/__init__.py
# Инициализация модуля inline, для создания inline-команд

from aiogram import Router
from .reklama import router as reklama_router

# Объявление главного роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="inline_routers")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    reklama_router,
)