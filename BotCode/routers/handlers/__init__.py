# BotCode/routers/handlers/__init__.py
# Инициализация модуля handlers, для работы со специфическими сообщениями

from aiogram import Router
from .new_member_notification import router as member_notification_router
from .leave_member import router as leave_member_router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="handlers_head_router")

# Идет самым последним, если другие роутеры не сработали
router.include_routers(
    member_notification_router,
    leave_member_router,
)
