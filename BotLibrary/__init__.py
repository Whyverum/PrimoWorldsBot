# BotLibrary/__init__.py
# Инициализация пакета BotLibrary, для настройки личных библиотек проекта

# Экспортирование модулей во внешние слои проекта
from .analytics import *
from .loggers import *
from .samples import *
from .system import *
from .timer import *
from .validators import *

from SQLite3 import create_user_db
from ProjectsFiles import Permissions


# Функция установки
async def setup():
    # Запуск логеров
    await setup_logger()

    # Получение информации о боте
    await bot_get_info()

    # Вывод сообщение о запуске
    Logs.start(text=f"Начало запуска бота @{BotInfo.username}...")
    Logs.console()

    # Автоматическое создание базы данных при отсутствии
    await create_user_db()

    # Создание пустых директорий
    await setup_directories()

    # Нужно ли удалить веб-хук
    if Permissions.delete_webhook:
        await bot.delete_webhook()

    await set_adm_rights()
    await set_bot_name()
    await set_bot_description()
    await set_bot_short_description()
