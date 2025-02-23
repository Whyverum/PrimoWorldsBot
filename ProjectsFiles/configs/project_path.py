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

    # Названия директорий для аватарок
    user_avatar : str = "Users"
    chat_avatar : str = "Chats"
    channel_avatar : str = "Channel"
    avatar_directories : List[str] = [user_avatar, chat_avatar, channel_avatar]


# Класс создания директорий проекта
class ProjectPath:
    """
    Класс для хранения путей к проектам и логам.
    """
    BotLogs : str = "BotLogs"
    bot_info_log_file: str = f"{BotLogs}/bot_info.log"
    start_log_file: str = f"{BotLogs}/start.log"
    debug_log_file: str = f"{BotLogs}/debug.log"
    info_log_file : str = f"{BotLogs}/info.log"
    warning_log_file: str = f"{BotLogs}/warning.log"
    error_log_file: str = f"{BotLogs}/error.log"

    BotFiles : str = "BotFiles"
    received_media : str = f"{BotFiles}/media"
    received_avatars : str = f"{BotFiles}/avatars"

    personal_media : str = "ProjectsFiles/media"
