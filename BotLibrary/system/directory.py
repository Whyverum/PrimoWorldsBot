# BotLibrary/system/directory.py
# Создание пустых директорий при первом запуске

import os
from typing import List
from ProjectsFiles import ProjectPath, TypeDirectory

# Настройка экспорта из модуля
__all__ = ("Directory",)

class Directory:
    @staticmethod
    async def create_directory(directory: str) -> None:
        """
        Создает директории, если они еще не существуют.

        :param directory: Путь к базовой директории.
        :return: Создание директорий по определенному пути.
        """
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    async def create_directories(base_directory: str, subdirectories: List[str]) -> None:
        """
        Создает указанные поддиректории в указанной базовой директории.

        :param base_directory: Путь к базовой директории.
        :param subdirectories: Список поддиректорий, которые необходимо создать.
        :return: Создание директорий по определенному пути.
        """
        # Создание директорий и файлов в каждой из них
        for subdirectory in subdirectories:
            directory_path = os.path.join(base_directory, subdirectory)

            # Проверка, существует ли директория, если нет - создаём
            os.makedirs(directory_path, exist_ok=True)

    @staticmethod
    async def setup() -> None:
        """
        Настройка начальных пустых директорий для проекта.

        :return: Создание системы директорий по определенному пути.
        """
        # Создание директорий для медиа файлов
        await Directory.create_directories(ProjectPath.personal_media, TypeDirectory.media_directories)
        await Directory.create_directories(ProjectPath.received_media, TypeDirectory.media_directories)
        await Directory.create_directories(ProjectPath.received_avatars, TypeDirectory.avatar_directories)
