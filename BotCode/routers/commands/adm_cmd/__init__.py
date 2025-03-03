# BotCode/routers/commands/adm_cmd/__init__.py
# Инициализация модуля adm_cmd, для административных команд бота

# Экспортирование модулей во внешние слои проекта
from aiogram import Router
from .all_cmd import all_cmd
from .ban_cmd import ban_cmd

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="adm_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    ban_cmd.router,
    all_cmd.router,
)
