# BotLibrary/system/bot_edit.py
# Под-пакет установки настроек бота

from aiogram import Bot
from ProjectsFiles import BotEdit

# Настройка экспорта из модуля
__all__ = ("BotRights",)

class BotRights:
    """
    Класс для установки прав администратора и метаинформации бота (имя, описания).
    """
    @staticmethod
    async def set_administrator_rights(bot: Bot) -> None:
        """
        Установка прав администратора в чатах.

        :param bot: Базовый объект бота.
        :return: Измененные права по конфигу.
        """
        from aiogram.types import ChatAdministratorRights
        rights: ChatAdministratorRights = ChatAdministratorRights(
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

        current_rights: ChatAdministratorRights = await bot.get_my_default_administrator_rights()
        if current_rights != rights:
            await bot.set_my_default_administrator_rights(rights)

    @staticmethod
    async def set_name(bot: Bot) -> None:
        """
        Установка имени бота.

        :param bot: Базовый объект бота.
        :return: Измененное имя бота.
        """
        current_name: str = (await bot.get_me()).first_name
        new_name: str = str(BotEdit.name)

        if not (1 <= len(new_name) <= 32):
            from ..loggers import Logs
            Logs.error(log_type="SET_NAME", user="BOT", text="Имя бота должно быть от 1 до 32 символов.")
            return

        if current_name != new_name:
            await bot.set_my_name(new_name)

    @staticmethod
    async def set_description(bot: Bot) -> None:
        """
        Установка описания бота.

        :param bot: Базовый объект бота.
        :return: Измененное описание бота.
        """
        from aiogram.types import BotDescription
        current_description: BotDescription = await bot.get_my_description()
        new_description: str = str(BotEdit.description)

        if not (0 < len(new_description) <= 255):
            from ..loggers import Logs
            Logs.error(log_type="SET_DESCRIPTION", user="BOT", text="Описание должно быть от 1 до 255 символов.")
            return

        if current_description != new_description:
            await bot.set_my_description(description=new_description)

    @staticmethod
    async def set_short_description(bot: Bot) -> None:
        """
        Установка описания виджета.

        :param bot: Базовый объект бота.
        :return: Измененное описание виджета бота.
        """
        from aiogram.types import BotShortDescription
        current_short_description: BotShortDescription = await bot.get_my_short_description()
        new_short_description: str = str(BotEdit.short_description)

        if not (0 < len(new_short_description) <= 512):
            from ..loggers import Logs
            Logs.error(log_type="SET_SHORT_DESCRIPTION", user="BOT", text="Короткое описание должно быть от 1 до 512 символов.")
            return

        if current_short_description != new_short_description:
            await bot.set_my_short_description(short_description=new_short_description)

    @staticmethod
    async def all(bot: Bot) -> None:
        """
        Применяет все настройки: права, имя, описание и короткое описание.

        :param bot: Базовый объект бота.
        :return: Изменение всех основных параметров бота.
        """
        await BotRights.set_administrator_rights(bot)
        await BotRights.set_name(bot)
        await BotRights.set_description(bot)
        await BotRights.set_short_description(bot)
