# BotCode/routers/commands/easteggs_cmd/__init__.py
# Инициализация модуля easteggs_cmd, для пасхальных команд бота

# Экспортирование модулей во внешние слои проекта
from aiogram import Router
from .polina_anketa import polina_za_tri_eleksira_cmd
from .kataz_pidaraz_2020 import kataz_pidaraz_2020_cmd
from .finaki_succub import finaki_succub_cmd

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="easteggs_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    polina_za_tri_eleksira_cmd.router,
    kataz_pidaraz_2020_cmd.router,
    finaki_succub_cmd.router,
)
