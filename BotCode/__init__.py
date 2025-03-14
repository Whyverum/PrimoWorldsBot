# BotCode/__init__.py
# Инициализация пакета BotCode, для работы с главными частями кода

from aiogram import Router
from .routers import router as all_routers
from .inline import router as inline_routers

# Объявление главного роутера
router = Router(name="main_router")

# Список подключаемых роутеров сверху-вниз
router.include_routers(
    all_routers,
            inline_routers,
)