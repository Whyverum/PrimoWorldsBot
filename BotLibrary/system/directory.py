# BotLibrary/system/directory.py
# Создание пустых директорий при первом запуске

import os
from ProjectsFiles import ProjectPath, TypeDirectory
from typing import List

# Настройка экспорта из модуля
__all__ = ("create_directories", "setup_directories", "create_directory")


# Функция создания директории
async def create_directory(directory : str) -> None:
    os.makedirs(directory)


# Функция создания поддиректорий
async def create_directories(base_directory: str, subdirectories: List[str]) -> None:
    """
    Создает указанные поддиректории в указанной базовой директории, если они еще не существуют.

    :param base_directory: Путь к базовой директории.
    :param subdirectories: Список поддиректорий, которые необходимо создать.
    """
    # Создание директорий и файлов в каждой из них
    for subdirectory in subdirectories:
        directory_path = os.path.join(base_directory, subdirectory)

        # Проверка, существует ли директория, если нет - создаём
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)


# Функция установки начальных директорий
async def setup_directories() -> None:
    """
    Настройка начальных пустых директорий для проекта.
    """
    # Создание директорий для медиа файлов
    await create_directories(ProjectPath.personal_media, TypeDirectory.media_directories)
    await create_directories(ProjectPath.received_media, TypeDirectory.media_directories)
    await create_directories(ProjectPath.received_avatars, TypeDirectory.avatar_directories)
    # await create_directories(ProjectPath.msg, TypeDirectory.msg_directories)
