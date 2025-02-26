# ProjectsFiles/configs/logs_config.py
# Конфиги настройки логов

from .config import Permissions

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


    # Шаблон логов для старта
    start_text: str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>|</red> "
        "<blue>{extra[system]}-{extra[log_type]}</blue> <red>|</red> "
        "<red>{extra[user]} |</red> <bold>{message}</bold>"
    )

    # Шаблон логов для отладки
    debug_text : str = (
        "<cyan>{time:YYYY-MM-DD HH:mm:ss}</cyan> <red>|</red> "
        "<magenta>{extra[system]}-{extra[log_type]}</magenta> <red>|</red> "
        "<yellow>{extra[user]}</yellow> <red>|</red> <level>{message}</level>"
    )

    # Шаблон логов для информации
    info_text : str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>|</red> "
        "<blue>{extra[system]}-{extra[log_type]}</blue> <red>|</red> "
        "<red>{extra[user]} |</red> <level>{message}</level>"
    )

    # Шаблон логов для предупреждений
    warning_text : str = (
        "<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> <red>|</red> "
        "<yellow>{extra[system]}-{extra[log_type]}</yellow> <red>|</red> "
        "<red>{extra[user]} |</red> <level>{message}</level>"
    )

    # Шаблон логов для ошибок
    error_text : str = (
        "<level>{time:YYYY-MM-DD HH:mm:ss} | "
        "<bold>{extra[system]}-{extra[log_type]}</bold> | "
        "{extra[user]} | {message}</level>"
    )
