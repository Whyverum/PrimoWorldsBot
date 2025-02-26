# BotCode/routers/common/__init__.py
# Инициализация пакета common, для работы со всеми сообщениями

from aiogram import Router
from .messages import router as common_messages_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="common_head_router")

# Идет самым последним, если другие роутеры не сработали
router.include_router(common_messages_router)
