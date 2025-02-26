# BotCode/routers/handlers/__init__.py
# Инициализация пакета handlers, для работы со всеми сообщениями

from aiogram import Router
from .new_member_notification import router as member_notification_router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="handlers_head_router")

# Идет самым последним, если другие роутеры не сработали
router.include_router(member_notification_router)
