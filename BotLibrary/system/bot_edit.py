# BotLibrary/system/bot_edit.py
# Под-пакет установки настроек бота

from aiogram.types import ChatAdministratorRights
from ProjectsFiles import BotEdit
from .bots import bot

# Настройка логирования
log_type = "Edit"

# Настройка экспорта из модуля
__all__ = ("set_adm_rights", "set_bot_name", "set_bot_description", "set_bot_short_description")

# Функция установки прав администратора
async def set_adm_rights() -> None:
    """
    Устанавливает права администратора для бота, если они отличаются от текущих.

    :return: Изменение прав администратора
    """
    rights = ChatAdministratorRights(
        is_anonymous=BotEdit.is_anonymous,
        can_manage_chat=BotEdit.manage_chat,
        can_delete_messages=BotEdit.delete_messages,
        can_manage_video_chats=BotEdit.manage_video_chats,
        can_restrict_members=BotEdit.restrict_members,
        can_promote_members=BotEdit.promote_members,
        can_change_info=BotEdit.change_info,
        can_invite_users=BotEdit.invite_users,
        can_post_stories=BotEdit.post_stories,
        can_edit_stories=BotEdit.edit_stories,
        can_delete_stories=BotEdit.delete_stories,
        can_post_messages=BotEdit.post_messages,
        can_edit_messages=BotEdit.edit_messages,
        can_pin_messages=BotEdit.pin_messages,
        can_manage_topics=BotEdit.manage_topics,
    )

    # Применяем права только в случае изменения
    current_rights = await bot.get_my_default_administrator_rights()
    if current_rights != rights:
        await bot.set_my_default_administrator_rights(rights)


# Функция установки имени бота с проверкой на ограничения
async def set_bot_name(new_name: str = BotEdit.name) -> None:
    """
    Устанавливает имя бота, если оно отличается от текущего и соответствует ограничениям.

    :param new_name: Новое имя бота (config)
    :return: Имя бота
    """
    # Импортируем Logs внутри функции, чтобы избежать циклического импорта
    from ..loggers.custom_loggers import Logs

    # Получаем текущее имя бота
    current_name = (await bot.get_me()).first_name

    # Проверка длины имени
    if len(new_name) < 1 or len(new_name) > 32:
        Logs.error(log_type=log_type, user="NAME_BOT", text="Имя бота должно быть от 1 до 32 символов.")
        return  # Выходим из функции, если имя некорректно

    # Проверяем, совпадает ли текущее имя с тем, которое мы хотим установить
    if current_name != new_name:
        await bot.set_my_name(new_name)


# Функция установки описания бота с проверкой на ограничения
async def set_bot_description(new_description: str = BotEdit.description) -> None:
    """
    Устанавливает описание бота, если оно отличается от текущего и соответствует ограничениям.

    :param new_description: Новое описание для бота (config)
    :return: Описание бота
    """
    # Импортируем Logs внутри функции, чтобы избежать циклического импорта
    from ..loggers.custom_loggers import Logs

    # Получаем текущее описание бота
    current_description = await bot.get_my_description()

    # Проверка длины описания
    if len(new_description) > 255 or len(new_description)==0:
        Logs.error(log_type=log_type, user="DISCRIPT", text="Короткое описание бота не может превышать 255 символов или быть равно 0.")
        return  # Выходим из функции, если описание некорректно

    # Проверяем, совпадает ли текущее описание с тем, которое мы хотим установить
    if current_description != new_description:
        await bot.set_my_description(description=new_description)


# Функция установки короткого описания бота с проверкой на ограничения
async def set_bot_short_description(new_short_description: str = BotEdit.short_description) -> None:
    """
    Устанавливает короткое описание бота, если оно отличается от текущего и соответствует ограничениям.

    :param new_short_description: Новое описание виджета для бота (config)
    :return: Короткое описание бота
    """
    # Импортируем Logs внутри функции, чтобы избежать циклического импорта
    from ..loggers.custom_loggers import Logs

    # Получаем текущее короткое описание бота
    current_short_description = await bot.get_my_short_description()

    # Проверка длины короткого описания
    if len(new_short_description) > 512 or len(new_short_description) == 0:
        Logs.error(log_type=log_type, user="SHORT_DISCRIPT", text="Описание виджета не может превышать 512 символов или быть равно 0.")
        return  # Выходим из функции, если короткое описание некорректно

    # Проверяем, совпадает ли текущее короткое описание с тем, которое мы хотим установить
    if current_short_description != new_short_description:
        await bot.set_my_short_description(short_description=new_short_description)