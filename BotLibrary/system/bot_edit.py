# BotLibrary/system/edit_bot.py
# Библиотека установки настроек бота через проект и конфиги

from aiogram.types import ChatAdministratorRights
from ProjectsFiles import BotEdit
from .bots import bot
from ..loggers import logger

# Настройка логирования
log_type = "Edit"

# Функция для выполнения всех настроек, если они не совпадают
async def set_all():
    await set_adm_rights()
    await set_bot_name()
    await set_bot_description()
    await set_bot_short_description()


# Функция установки прав администратора
async def set_adm_rights():
    # Применить права администратора для бота
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
async def set_bot_name():
    # Получаем текущее имя бота
    current_name = (await bot.get_me()).first_name

    # Проверка длины имени
    if len(BotEdit.name) < 1 or len(BotEdit.name) > 32:
        # Логируем ошибку, если имя не соответствует ограничению
        (logger.bind(log_type=log_type, user="NAME_BOT")
         .error("Имя бота должно быть от 1 до 32 символов."))

    # Проверяем, совпадает ли текущее имя с тем, которое мы хотим установить
    if current_name != BotEdit.name:
        await bot.set_my_name(BotEdit.name)


# Функция установки описания бота с проверкой на ограничения
async def set_bot_description():
    # Получаем текущее описание бота
    current_description = await bot.get_my_description()

    # Проверка длины описания
    if len(BotEdit.description) > 255:
        (logger.bind(log_type=log_type, user="DISCRIPT")
         .error("Короткое описание бота не может превышать 255 символов."))

    # Проверяем, совпадает ли текущее описание с тем, которое мы хотим установить
    if current_description != BotEdit.description:
        await bot.set_my_description(description=BotEdit.description)


# Функция установки короткого описания бота с проверкой на ограничения
async def set_bot_short_description():
    # Получаем текущее короткое описание бота
    current_short_description = await bot.get_my_short_description()

    # Проверка длины короткого описания
    if len(BotEdit.short_description) > 512:
        (logger.bind(log_type=log_type, user="SHORT_DISCRIPT")
         .error("Описание виджета не может превышать 512 символов."))

    # Проверяем, совпадает ли текущее короткое описание с тем, которое мы хотим установить
    if current_short_description != BotEdit.short_description:
        await bot.set_my_short_description(short_description=BotEdit.short_description)
