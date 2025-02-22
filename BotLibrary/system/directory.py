# BotLibrary/system/directory.py
# Создание пустых директорий при первом запуске

import os
from ProjectsFiles import ProjectPath, TypeDirectory

# Настройка экспорта из модуля
__all__ = ("create_directories", "setup_directories")

# Функция создания пустых директорий
async def create_directories(base_directory, subdirectories):
    # Создание директорий и файлов в каждой из них
    for subdirectory in subdirectories:
        directory_path = os.path.join(base_directory, subdirectory)

        # Проверка, существует ли директория, если нет - создаём
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)


# Начальная установка пустых директорий
async def setup_directories():
    await create_directories(ProjectPath.personal_media, TypeDirectory.media_directories)
    # await create_directories(ProjectPath.received_media, TypeDirectory.media_directories)
    # await create_directories(ProjectPath.bot_files, TypeDirectory.avatar_directories)
    # await create_directories(ProjectPath.msg, TypeDirectory.msg_directories)