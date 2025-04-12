# BotLibrary/system/__init__.py
# Инициализация пакета system, для библиотек запуска

# Экспортирование модулей во внешние слои проекта
from .db_class import *
from ProjectsFiles import BotVar

# Создание экземпляра класса
db = Database(BotVar.bd_names)

# Создание базы данных
db.create_db()
