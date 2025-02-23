# ProjectsFiles/config.py
# Файл-хранилище всех конфигов и настроек для бота

from typing import List, Tuple

# Список разрешений для бота
class Permissions:
    """
    Класс для хранения настроек разрешений бота.
    """
    bot_edit : bool = False    # Разрешение на изменение имени, описания и виджета (True/False)
    delete_webhook : bool = True   # Разрешение на удаление веб-хука (True/False)

    logging : bool = True  # Разрешение на вывод логов в консоль (True/False)
    logging_to_file : bool = False     # Разрешение на вывод логов в файл (True/False)
    msg_logging : bool = False     # Логирование сообщений в консоль (В разработке)

    start_info_console : bool = True   # Вывод информации о боте в начале (True/False)

    sql_user : bool = True     # Разрешение на регистрацию в базе данных (True/False)


# Имя, описание и виджет бота(при наличии баннера виджета)
class BotEdit:
    """
    Класс для хранения данных о боте: имя, описание, разрешения и настройки.
    """
    # Разрешение на ведение логов
    permission : bool = Permissions.bot_edit
    name : str = "Стартовый бот"
    description : str = "Описание бота"
    short_description : str = "Описание виджета"

    is_anonymous : bool = False
    manage_chat : bool = True
    delete_messages : bool = True
    manage_video_chats : bool = True
    restrict_members : bool = True
    promote_members : bool = True
    change_info : bool = True
    invite_users : bool = True
    post_stories : bool = True
    edit_stories : bool = True
    delete_stories : bool = True
    post_messages : bool = True
    edit_messages : bool = True
    pin_messages : bool = True
    manage_topics : bool = True


# Хранение параметров проекта
class BotVar:
    """
    Класс для хранения глобальных параметров проекта.
    """
    encod : str = "utf-8"
    language : str = "Python3-Aiogram"
    time_format : str = "%Y-%m-%d %H:%M:%S"
    prefix : Tuple[str, ...] = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')


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
    personal_media : str = "ProjectsFiles/media"


# Настройки логирования бота
class BotLogs:
    """
    Класс для хранения параметров логирования: шаблоны логов, разрешения, размеры файлов и т. д.
    """
    # Разрешение на ведение логов
    permission : bool = Permissions.logging
    permission_to_file : bool = Permissions.logging_to_file
    permission_msg : bool = Permissions.msg_logging

    # Максимальный размер лог-файла
    max_size : str = "500 MB"

    # Шаблон логов для отладки
    debug_text : str = (
        "<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> <red>|</red> "
        "<magenta>DEBUG-{extra[log_type]}</magenta> <red>|</red> "
        "<yellow>{extra[user]} |</yellow> <level>{message}</level>"
    )

    # Шаблон логов для информации
    info_text : str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>|</red> "
        "<blue>PRIMO-{extra[log_type]}</blue> <red>|</red> "
        "<red>{extra[user]} |</red> <level>{message}</level>"
    )

    # Шаблон логов для предупреждений
    warning_text : str = (
        "<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <red>|</red> "
        "<yellow>WARNING-{extra[log_type]}</yellow> <red>|</red> "
        "<red>{extra[user]} |</red> <level>{message}</level>"
    )

    # Шаблон логов для ошибок
    error_text : str = (
        "<level>{time:YYYY-MM-DD HH:mm:ss} | "
        "<bold>ERROR-{extra[log_type]}</bold> | "
        "{extra[user]} | {message}</level>"
    )
