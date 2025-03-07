# BotCode/routers/commands/user_cmd/__init__.py
# Инициализация модуля user_cmd, для пользовательских команд бота

# Экспортирование модулей во внешние слои проекта
from aiogram import Router
from .start_cmd import start_cmd
from .start_time_cmd import start_time_cmd
from .help_cmd import help_cmd
from .weather_cmd import weather_cmd
from .stats import stats_cmd
from .my_cmd import my_cmd

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="user_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    help_cmd.router,
    start_time_cmd.router,
    weather_cmd.router,
    stats_cmd.router,
    my_cmd.router,
)

router.include_routers(start_cmd.router)
