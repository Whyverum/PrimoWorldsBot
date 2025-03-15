# BotCode/__init__.py
# Инициализация пакета BotCode, для работы с главными частями кода

from aiogram import Router
from .routers import router as all_routers
from .inline import router as inline_routers
from .easteggs import router as easteggs_router

# Объявление главного роутера
router = Router(name="main_router")

# Список подключаемых роутеров сверху-вниз
router.include_routers(
    inline_routers,
    easteggs_router,
)
router.include_router(all_routers)
