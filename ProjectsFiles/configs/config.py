# ProjectsFiles/config.py
# Файл-хранилище всех конфигов и настроек для бота

# Список разрешений для бота
class Permissions:
    bot_edit = False
    logging = True
    logging_to_file = False
    msg_logging = False


# Имя, описание и виджет бота(при наличии баннера виджета)
class BotEdit:
    # Разрешение на ведение логов
    permission = Permissions.bot_edit
    name = "Стартовый бот"
    description = "Описание бота"
    widget_description = "Описание виджета"


# Класс создания директорий проекта
class ProjectPath:
    BotLogs = "BotLogs"




# Настройки логирования бота
class BotLogs:
    # Разрешение на ведение логов
    permission = Permissions.logging
    permission_to_file = Permissions.logging_to_file
    permission_msg = Permissions.msg_logging

    # Максимальный размер лог-файла
    max_size = "500 MB"

    # Шаблон логов для отладки
    debug_text = (
        "<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> <red>|</red> "
        "<magenta>DEBUG-{extra[log_type]}</magenta> <red>|</red> "
        "<yellow>{extra[user]} |</yellow> <level>{message}</level>"
    )

    # Шаблон логов для информации
    info_text = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>|</red> "
        "<blue>PRIMO-{extra[log_type]}</blue> <red>|</red> "
        "<red>{extra[user]} |</red> <level>{message}</level>"
    )

    # Шаблон логов для предупреждений
    warning_text = (
        "<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <red>|</red> "
        "<orange>WARNING-{extra[log_type]}</orange> <red>|</red> "
        "<red>{extra[user]} |</red> <level>{message}</level>"
    )

    # Шаблон логов для ошибок
    error_text = (
        "<level>{time:YYYY-MM-DD HH:mm:ss} | "
        "<bold>ERROR-{extra[log_type]}</bold> | "
        "{extra[user]} | {message}</level>"
    )


# Хранение параметров проекта
class BotVar:
    encod = "utf-8"
    language = "Python3-Aiogram"
    time_format = "%Y-%m-%d %H:%M:%S"
    prefix = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')
