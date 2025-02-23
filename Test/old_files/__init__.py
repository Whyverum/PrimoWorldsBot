# BotCode/routers/old_files/__init__.py
# Инициализация старого пакета old_files, для хранения старых функций

from aiogram import Router
from .media_func import router as media_old_router
from .regular_handlers import router as regular_router


# Объявление роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="old_files_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    regular_router,
    media_old_router,
)


# Список подключаемых роутеров сверху-вниз
router.include_routers()
