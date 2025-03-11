# BotCode/easteggs/holidays/__init__.py
# Инициализация модуля holidays, для пасхальных поздравлений

# Экспортирование модулей во внешние слои проекта
from aiogram import Router
from .march8 import *

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="holidays_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    March8.router,
    March8_Finaki.router,
    March8_sleshik.router,
    March8_polina.router,
    March8_finik.router,
    March8_kataz.router,
)
