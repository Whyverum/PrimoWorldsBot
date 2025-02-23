# ProjectsFiles/configs/project_path.py
# Хранилище всех важных директорий

from typing import List

# Класс для хранения типов директорий
class TypeDirectory:
    """
    Класс для хранения типов сообщений и директорий, которые нужно создать.
    """
    # Типы сообщений и список директорий для создания
    private_msg : str = "Личные"
    group_msg : str = "Группы"

    # Названия директорий-хранилищ
    avatar : str = "Avatar"
    photo : str = "Photo"
    video : str = "Video"
    videonote : str = "VideoNote"
    gif : str = "GIF"
    files : str = "Document"
    voice : str = "Voice"
    media_directories : List[str] = [avatar, photo, video, videonote, gif, files, voice]


# Класс создания директорий проекта
class ProjectPath:
    """
    Класс для хранения путей к проектам и логам.
    """
    BotLogs : str = "BotLogs"
    start_log_file: str = f"{BotLogs}/start.log"
    debug_log_file: str = f"{BotLogs}/debug.log"
    info_log_file : str = f"{BotLogs}/info.log"
    warning_log_file: str = f"{BotLogs}/warning.log"
    error_log_file: str = f"{BotLogs}/error.log"
    logs_path : List[str] = [debug_log_file, info_log_file, warning_log_file, error_log_file]


    personal_media : str = "ProjectsFiles/media"
