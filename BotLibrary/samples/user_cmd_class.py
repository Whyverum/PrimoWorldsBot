# BotCode/routers/commands/user_cmd_class.py
# Класс-шаблон для создания новых команд

from aiogram import Router, types, F
from aiogram.enums import ChatAction
from aiogram.filters import Command

from ProjectsFiles import BotVar
from BotLibrary.validators import username
from BotLibrary.loggers import Logs

# Настройки экспорта в модули
__all__ = ("CommandHandler", )

# Класс-шаблон для команд
class CommandHandler:
    def __init__(self, name: str, keywords : list, chat_action : bool = False,
                 description: str = "Описание команды", text_msg : str = "Сообщение",
                 keyboard = None, prefix = BotVar.prefix, callbackdata = None,
                 ignore_case : bool = True, activate_keywoards : bool = True,
                 activate_commands : bool = True, activate_callback : bool = True,
                 media : str = "message", path_to_media : str = None, parse_mode : str = BotVar.parse_mode,
                 disable_notification : bool = False,
                 ):

        self.router = Router(name=f"{name}_router")
        self.name = name
        self.log_type = name.capitalize()
        self.description = description

        self.keywords = keywords
        self.text_msg = text_msg
        self.parse_mode = parse_mode
        self.keyboard = keyboard
        self.chat_action = chat_action
        self.disable_notification = disable_notification

        self.media = media.lower()
        self.path_to_media = path_to_media
        if callbackdata == "keywords":
            self.callbackdata = keywords
        else:
            self.callbackdata = callbackdata


        # Привязываем хэндлер к роутеру
        if activate_commands:
            self.router.message(Command(*keywords, prefix=prefix, ignore_case=ignore_case))(self.handler)
        if activate_keywoards:
            self.router.message(F.text.lower().in_(keywords))(self.handler)
        if activate_callback:
            self.router.message(F.text.lower().in_(callbackdata))(self.handler)


    async def handler(self, message: types.Message):
        """Основной хэндлер команды."""
        try:
            Logs.info(log_type=self.log_type, user=username(message), text=f"использовал(а) команду /{self.name}")
            if self.media == "message":
                await message.reply(
                    text=self.text_msg,
                    reply_markup=self.keyboard() if self.keyboard else None,
                    parse_mode=self.parse_mode,
                    disable_notification=self.disable_notification,
                )
                if self.chat_action:
                    await message.bot.send_chat_action(
                        chat_id=message.chat.id,
                        action=ChatAction.TYPING,
                    )
            else:
                if self.media == "photo":
                    await message.reply_photo(
                        photo="https://vos-mo.ru/upload/iblock/329/g0s939ge8o1n8xp7rcqnw9kkz9mcfrg2/risunok.jpg",
                        caption=self.text_msg)
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_PHOTO,
                        )

                if self.media == "gif":
                    await message.reply_animation(
                        animation="https://vos-mo.ru/upload/iblock/329/g0s939ge8o1n8xp7rcqnw9kkz9mcfrg2/risunok.jpg")
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_VIDEO,
                        )

                if self.media == "video":
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_VIDEO,
                        )

                if self.media == "videonote":
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_VIDEO_NOTE,
                        )

                if self.media == "audio":
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_VOICE,
                        )

                if self.media == "file":
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_DOCUMENT,
                        )

        # Проверка на ошибку
        except Exception as e:
            Logs.error(log_type=self.log_type, user=username(message), text=f"Ошибка команды: {e}")
