# BotCode/routers/__init__.py
# Инициализация пакета routers, для работы с асинхронными обработчиками

from aiogram import Router
from .commands import router as commands_head_router
from .common import router as common_head_router

# Объявление главного роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="all_routers")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    commands_head_router,
)

router.include_routers(common_head_router)
