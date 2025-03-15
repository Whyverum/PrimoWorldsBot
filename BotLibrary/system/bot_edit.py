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
async def set_adm_rights(anonym: bool = BotEdit.is_anonymous,
                         manage_chat: bool = BotEdit.manage_chat,
                         delete_msg: bool = BotEdit.delete_messages,
                         manage_video_chats: bool = BotEdit.manage_video_chats,
                         restrict_members: bool = BotEdit.restrict_members,
                         promote_members: bool = BotEdit.promote_members,
                         change_info: bool = BotEdit.change_info,
                         invite_users: bool = BotEdit.invite_users,
                         post_stories: bool = BotEdit.post_stories,
                         edit_stories: bool = BotEdit.edit_stories,
                         delete_stories: bool = BotEdit.delete_stories,
                         post_messages: bool = BotEdit.post_messages,
                         edit_messages: bool = BotEdit.edit_messages,
                         pin_messages: bool = BotEdit.pin_messages,
                         manage_topics: bool = BotEdit.manage_topics,) -> None:
    """
    Устанавливает права администратора для бота, если они отличаются от текущих.
    Все через конфиги!!!

    :param anonym: Позволяет ли боту быть анонимным.
    :param manage_chat: Разрешение на управление чатом.
    :param delete_msg: Разрешение на удаление сообщений.
    :param manage_video_chats: Разрешение на управление видеочатами.
    :param restrict_members: Разрешение на ограничение участников (мут, бан).
    :param promote_members: Разрешение на назначение администраторов.
    :param change_info: Разрешение на изменение информации о группе/канале.
    :param invite_users: Разрешение на приглашение новых участников.
    :param post_stories: Разрешение на публикацию историй.
    :param edit_stories: Разрешение на редактирование историй.
    :param delete_stories: Разрешение на удаление историй.
    :param post_messages: Разрешение на публикацию сообщений (только для каналов).
    :param edit_messages: Разрешение на редактирование сообщений (только для каналов).
    :param pin_messages: Разрешение на закрепление сообщений.
    :param manage_topics: Разрешение на управление темами (в супергруппах).

    :return: Изменение прав администратора
    """
    rights = ChatAdministratorRights(
        is_anonymous=anonym,
        can_manage_chat=manage_chat,
        can_delete_messages=delete_msg,
        can_manage_video_chats=manage_video_chats,
        can_restrict_members=restrict_members,
        can_promote_members=promote_members,
        can_change_info=change_info,
        can_invite_users=invite_users,
        can_post_stories=post_stories,
        can_edit_stories=edit_stories,
        can_delete_stories=delete_stories,
        can_post_messages=post_messages,
        can_edit_messages=edit_messages,
        can_pin_messages=pin_messages,
        can_manage_topics=manage_topics,
    )

    # Применяем права только в случае изменения
    current_rights = await bot.get_my_default_administrator_rights()
    if current_rights != rights:
        await bot.set_my_default_administrator_rights(rights)
    else:
        return


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
    else:
        return


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
    else:
        return


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
    else:
        return
