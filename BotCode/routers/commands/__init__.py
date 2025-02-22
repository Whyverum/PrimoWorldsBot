# BotCode/routers/commands/__init__.py
# Инициализация модуля commands, для основных команд бота

from aiogram import Router
from .user_cmd import router as user_cmd_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="commands_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    user_cmd_router,
)