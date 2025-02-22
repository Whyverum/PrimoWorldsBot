# BotCode/routers/servey/__init__.py
# Инициализация пакета servey, для работы с последствиями

from aiogram import Router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="servey_head_router")

# Идет самым последним, если другие роутеры не сработали
router.include_routers(

)
