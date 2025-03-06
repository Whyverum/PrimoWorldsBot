# BotCode/routers/commands/__init__.py
# Инициализация модуля commands, для основных команд бота

from aiogram import Router
from .user_cmd import router as user_cmd_router
from .adm_cmd import router as adm_cmd_router
from .easteggs_cmd import router as easteggs_cmd_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="commands_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    adm_cmd_router,
    user_cmd_router,
    easteggs_cmd_router,
)