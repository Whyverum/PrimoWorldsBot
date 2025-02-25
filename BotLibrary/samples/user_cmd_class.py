# BotCode/routers/commands/user_cmd_class.py
# Класс-шаблон для создания новых команд

from aiogram import Router, types, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import InputMediaPhoto

from BotLibrary import valid_url
from ProjectsFiles import BotVar
from BotLibrary.validators import username
from BotLibrary.loggers import Logs

# Настройки экспорта в модули
__all__ = ("CommandHandler",)


# Класс-шаблон для команд
class CommandHandler:
    def __init__(self, name: str, keywords: list, func=None, text_msg: str = None, chat_action: bool = False,
                 description: str = "Описание команды", tg_links: bool = False,
                 keyboard=None, prefix=BotVar.prefix, callbackdata=None,
                 ignore_case: bool = True, activate_keywoards: bool = True,
                 activate_commands: bool = True, activate_callback: bool = True,
                 media: str = "message", path_to_media=None, parse_mode: str = BotVar.parse_mode,
                 disable_notification: bool = False, protect: bool = True, ):

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
        self.protect = protect
        self.func = func

        # Поддержка до 10 медиафайлов через список
        if path_to_media is None:
            self.path_to_media = []
        elif isinstance(path_to_media, (str, types.FSInputFile)):
            self.path_to_media = [path_to_media]
        elif isinstance(path_to_media, list):
            self.path_to_media = path_to_media[:10]  # Ограничение до 10 элементов
        self.tg_links = tg_links

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
            if self.func:
                await self.func(message)  # Вызов переданной функции, если она есть
            if self.tg_links:
                self.text_msg = self.text_msg.replace("<users>", str(message.from_user.id))

            Logs.info(log_type=self.log_type, user=username(message), text=f"использовал(а) команду /{self.name}")

            if self.media == "message":
                await message.reply(
                    text=self.text_msg,
                    reply_markup=self.keyboard() if self.keyboard else None,
                    parse_mode=self.parse_mode,
                    disable_notification=self.disable_notification,
                    has_protected_content=self.protect,
                )
                if self.chat_action:
                    await message.bot.send_chat_action(
                        chat_id=message.chat.id,
                        action=ChatAction.TYPING,
                    )
            else:
                if self.media == "photo" and len(self.path_to_media) > 1:
                    # Отправка медиагруппы для фотографий
                    media_group = []
                    for media_path in self.path_to_media:
                        url = valid_url(media_path)
                        if url:
                            media_group.append(InputMediaPhoto(media=media_path))
                        else:
                            media_group.append(InputMediaPhoto(media=types.FSInputFile(path=media_path)))

                    # Добавляем подпись и клавиатуру к последнему элементу
                    media_group[-1].caption = self.text_msg
                    media_group[-1].parse_mode = self.parse_mode

                    await message.reply_media_group(
                        media=media_group,
                        disable_notification=self.disable_notification,
                        has_protected_content=self.protect,

                    )
                    # Отправка клавиатуры отдельным сообщением, если есть
                    if self.keyboard:
                        await message.reply(
                            text=" ",
                            reply_markup=self.keyboard(),
                            disable_notification=self.disable_notification,
                        )
                    if self.chat_action:
                        await message.bot.send_chat_action(
                            chat_id=message.chat.id,
                            action=ChatAction.UPLOAD_PHOTO,
                        )
                else:
                    # Одиночное медиа или другие типы
                    for idx, media_path in enumerate(self.path_to_media):
                        is_last = idx == len(self.path_to_media) - 1
                        url = valid_url(media_path)

                        if self.media == "photo":
                            if url:
                                await message.reply_photo(
                                    photo=media_path,
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            else:
                                await message.reply_photo(
                                    photo=types.FSInputFile(path=media_path),
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            if self.chat_action and is_last:
                                await message.bot.send_chat_action(
                                    chat_id=message.chat.id,
                                    action=ChatAction.UPLOAD_PHOTO,
                                )

                        elif self.media == "gif":
                            if url:
                                await message.reply_animation(
                                    animation=media_path,
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            else:
                                await message.reply_animation(
                                    animation=types.FSInputFile(path=media_path),
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            if self.chat_action and is_last:
                                await message.bot.send_chat_action(
                                    chat_id=message.chat.id,
                                    action=ChatAction.UPLOAD_VIDEO,
                                )

                        elif self.media == "video":
                            if url:
                                await message.reply_video(
                                    video=media_path,
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            else:
                                await message.reply_video(
                                    video=types.FSInputFile(path=media_path),
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            if self.chat_action and is_last:
                                await message.bot.send_chat_action(
                                    chat_id=message.chat.id,
                                    action=ChatAction.UPLOAD_VIDEO,
                                )

                        elif self.media == "videonote":
                            if url:
                                await message.reply_video_note(
                                    video_note=media_path,
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            else:
                                await message.reply_video_note(
                                    video_note=types.FSInputFile(path=media_path),
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            if self.chat_action and is_last:
                                await message.bot.send_chat_action(
                                    chat_id=message.chat.id,
                                    action=ChatAction.UPLOAD_VIDEO_NOTE,
                                )

                        elif self.media == "audio":
                            if url:
                                await message.reply_audio(
                                    audio=media_path,
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            else:
                                await message.reply_audio(
                                    audio=types.FSInputFile(path=media_path),
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            if self.chat_action and is_last:
                                await message.bot.send_chat_action(
                                    chat_id=message.chat.id,
                                    action=ChatAction.UPLOAD_VOICE,
                                )

                        elif self.media == "file":
                            if url:
                                await message.reply_document(
                                    document=media_path,
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            else:
                                await message.reply_document(
                                    document=types.FSInputFile(path=media_path),
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                )
                            if self.chat_action and is_last:
                                await message.bot.send_chat_action(
                                    chat_id=message.chat.id,
                                    action=ChatAction.UPLOAD_DOCUMENT,
                                )

                            elif self.media == "dice":
                                await message.reply_dice(
                                    emoji="🎲",  # Эмодзи кубика как стандартное значение, если нет URL
                                    caption=self.text_msg if is_last else None,
                                    reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                    parse_mode=self.parse_mode,
                                    disable_notification=self.disable_notification,
                                    protect_content=self.protect,
                                    )

                                if self.chat_action and is_last:
                                    await message.bot.send_chat_action(
                                        chat_id=message.chat.id,
                                        action=ChatAction.CHOOSE_STICKER,
                                    )


        # Проверка на ошибку
        except Exception as e:
            Logs.error(log_type=self.log_type, text=f"Ошибка команды: {e}")
