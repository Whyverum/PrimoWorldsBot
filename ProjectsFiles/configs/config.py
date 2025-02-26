# ProjectsFiles/config.py
# Файл-хранилище всех конфигов и настроек для бота

from typing import Tuple

# Список разрешений для бота
class Permissions:
    """
    Класс для хранения настроек разрешений бота.
    """
    bot_edit: bool = True    # Разрешение на изменение имени, описания и виджета (True/False)
    delete_webhook: bool = True   # Разрешение на удаление веб-хука (True/False)

    logging: bool = True  # Разрешение на вывод логов в консоль (True/False)
    logging_to_file: bool = True     # Разрешение на вывод логов в файл (True/False)
    msg_logging: bool = False     # Логирование сообщений в консоль (В разработке)

    new_user: bool = True
    leave_user: bool = True

    start_info_console: bool = True   # Вывод информации о боте в начале (True/False)
    start_info_to_file: bool = True    # Вывод информации о боте в файл (True/False)

    sql_user: bool = True     # Разрешение на регистрацию в базе данных (True/False)


# Имя, описание и виджет бота(при наличии баннера виджета)
class BotEdit:
    """
    Класс для хранения данных о боте: имя, описание, разрешения и настройки.
    """
    # Разрешение на ведение логов
    project_name: str = "Свалка Флуд"
    permission: bool = Permissions.bot_edit
    name: str = "Стартовый бот"
    description: str = "Описание бота"
    short_description: str = "Описание виджета"

    is_anonymous: bool = False
    manage_chat: bool = True
    delete_messages: bool = True
    manage_video_chats: bool = True
    restrict_members: bool = True
    promote_members: bool = True
    change_info: bool = True
    invite_users: bool = True
    post_stories: bool = True
    edit_stories: bool = True
    delete_stories: bool = True
    post_messages: bool = True
    edit_messages: bool = True
    pin_messages: bool = True
    manage_topics: bool = True


# Хранение параметров проекта
class BotVar:
    """
    Класс для хранения глобальных параметров проекта.
    """
    encod: str = "utf-8"
    language: str = "Python3-Aiogram"
    time_format: str = "%Y-%m-%d %H:%M:%S"
    prefix: Tuple[str, ...] = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')

    parse_mode: str = "HTML"  # Устанавливаем формат HTML для всех сообщений
    disable_notification: bool = False  # Отключаем уведомления при отправке сообщений
    protect_content: bool = False  # Защищаем содержимое сообщений от копирования
    allow_sending_without_reply: bool = True  # Разрешаем отправлять сообщения без ответа на другое сообщение
    link_preview_is_disabled: bool = False  # Отключаем предварительный просмотр ссылок
    link_preview_prefer_small_media: bool = False
    link_preview_prefer_large_media: bool = True
    link_preview_show_above_text: bool = False
    show_caption_above_media: bool = False  # Показываем подпись выше медиа
