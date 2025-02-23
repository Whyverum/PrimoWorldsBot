# Test/__init__.py
# Инициализация пакета Test, для работы с тестированием  (в разработке)

# Импортируем библиотеки для экспорта
from aiogram import Router
from .commands import *
from .GUI import *
from .old_files import *


# Создание роутера "test_router"
router = Router(name="test_router")
