# BotCode/routers/commands/user_cmd_class.py
# Класс-шаблон для создания новых команд

import inspect
from aiogram import Router, types, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import InputMediaPhoto, InputMediaVideo, InputMediaDocument
from typing import Optional, Callable

from ..loggers import Logs
from ..validators import username, valid_url
from ProjectsFiles import BotVar
from SQLite3 import base_sql

# Настройки экспорта в модули
__all__ = ("CommandHandler",)

class CommandHandler:
    def __init__(self, name: str,
                 keywords: list,
                 func: Optional[list[Callable]] = None,
                 text_msg=None,
                 chat_action: bool = False,
                 description: str = "Описание команды",
                 tg_links: bool = False,
                 keyboard=None,
                 prefix=BotVar.prefix,
                 callbackdata: list = None,
                 only_admin: bool = False,
                 ignore_case: bool = True,
                 activate_keywords: bool = True,
                 delete_msg: bool = False,
                 activate_commands: bool = True,
                 activate_callback: bool = True,
                 media: str = "message",
                 path_to_media=None,
                 parse_mode: str = BotVar.parse_mode,
                 disable_notification: bool = BotVar.disable_notification,
                 protect: bool = BotVar.protect_content):
        self.router = Router(name=f"{name}_router")
        self.name = name
        self.log_type = name.capitalize()
        self.description = description
        self.last_bot_message = {}  # {chat_id: message_id}

        self.keywords = keywords
        self.text_msg = text_msg
        self.parse_mode = parse_mode
        self.keyboard = keyboard
        self.chat_action = chat_action
        self.disable_notification = disable_notification

        self.media = media.lower()
        self.protect = protect
        self.only_admin = only_admin
        self.func = func
        self.delete_msg = delete_msg

        # Поддержка до 10 медиафайлов через список
        if path_to_media is None:
            self.path_to_media = []
        elif isinstance(path_to_media, (str, types.FSInputFile)):
            self.path_to_media = [path_to_media]
        elif isinstance(path_to_media, list):
            self.path_to_media = path_to_media[:10]  # Ограничение до 10 элементов
        self.tg_links = tg_links

        if callbackdata:
            self.callbackdata = callbackdata
        else:
            self.callbackdata = keywords

        # Привязываем хэндлер к роутеру
        if activate_commands:
            self.router.message(Command(*keywords, prefix=prefix, ignore_case=ignore_case))(self.handler)
        if activate_keywords:
            self.router.message(F.text.lower().in_(keywords))(self.handler)
        if activate_callback and self.callbackdata:
            self.router.callback_query(F.data.in_(self.callbackdata))(self.callback_handler)

    async def callback_handler(self, callback: types.CallbackQuery):
        """Обработчик callback-запросов."""
        await self.handler(callback.message)  # Передаем сообщение в основном обработчике
        await callback.answer()  # Закрываем callback-запрос

    async def handler(self, message: types.Message):
        """Основной хэндлер команды."""
        try:
            # Извлекаем текст после команды
            command_text = (message.text or "").strip()  # Защита от NoneType
            args = command_text.split() if command_text else []  # Если текст есть — разделяем, иначе пустой список

            # Проверка на выполнение дополнительной функции (если она есть)
            if self.func:  # Проверяем, что функция не None
                # Выполняем все функции из списка, передавая команду
                for func_item in self.func:
                    # Используем inspect для получения информации о функции
                    if callable(func_item):
                        signature = inspect.signature(func_item)
                        # Если функция ожидает аргументы
                        if len(signature.parameters) > 0:
                            await func_item(message, *args)  # Передаем аргументы функции
                        else:
                            await func_item(message)  # Если функция не требует аргументов, просто вызываем её

            # Обрабатываем текстовое сообщение
            if callable(self.text_msg):
                text = self.text_msg()
            else:
                text = self.text_msg

            # Обрабатываем tg_links
            if self.tg_links:
                text = text.replace("<users>", str(message.from_user.id))

            # Обрабатываем текстовое сообщение
            if callable(self.text_msg):
                text = self.text_msg()
            else:
                text = self.text_msg

            # Обрабатываем tg_links
            if self.tg_links:
                text = text.replace("<users>", str(message.from_user.id))

            Logs.info(log_type=self.log_type, user=username(message), text=f"использовал(а) команду /{self.name}")
            await base_sql(message)

            # Обрабатываем текстовое сообщение
            if callable(self.text_msg):
                text = self.text_msg()
            else:
                text = self.text_msg

            # Обрабатываем tg_links
            if self.tg_links:
                text = text.replace("<users>", str(message.from_user.id))

            sent_msg = None
            if self.media == "message":
                sent_msg = await message.reply(
                    text=text,
                    reply_markup=self.keyboard() if self.keyboard else None,
                    parse_mode=self.parse_mode,
                    disable_notification=self.disable_notification,
                    protect_content=self.protect,
                )
                self.last_bot_message[message.chat.id] = sent_msg.message_id
                if self.chat_action:
                    await message.bot.send_chat_action(
                        chat_id=message.chat.id,
                        action=ChatAction.TYPING,
                    )
            elif self.media == "photo" and len(self.path_to_media) > 1:
                # Отправка медиагруппы для фотографий
                media_group = []
                for media_path in self.path_to_media:
                    url = valid_url(media_path)
                    if url:
                        media_group.append(InputMediaPhoto(media=media_path))
                    else:
                        media_group.append(InputMediaPhoto(media=types.FSInputFile(path=media_path)))

                # Добавляем подпись и клавиатуру к последнему элементу
                media_group[-1].caption = text
                media_group[-1].parse_mode = self.parse_mode

                sent_msg = await message.reply_media_group(
                    media=media_group,
                    disable_notification=self.disable_notification,
                    protect_content=self.protect,
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
            elif self.media == "video" and len(self.path_to_media) > 1:
                # Отправка медиагруппы для видео
                media_group = []
                for media_path in self.path_to_media:
                    url = valid_url(media_path)
                    if url:
                        media_group.append(InputMediaVideo(media=media_path))
                    else:
                        media_group.append(InputMediaVideo(media=types.FSInputFile(path=media_path)))

                # Добавляем подпись и клавиатуру к последнему элементу
                media_group[-1].caption = text
                media_group[-1].parse_mode = self.parse_mode

                sent_msg = await message.reply_media_group(
                    media=media_group,
                    disable_notification=self.disable_notification,
                    protect_content=self.protect,
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
                        action=ChatAction.UPLOAD_VIDEO,
                    )
            elif self.media == "file" and len(self.path_to_media) > 1:
                # Отправка медиагруппы для файлов
                media_group = []
                for media_path in self.path_to_media:
                    url = valid_url(media_path)
                    if url:
                        media_group.append(InputMediaDocument(media=media_path))
                    else:
                        media_group.append(InputMediaDocument(media=types.FSInputFile(path=media_path)))

                # Добавляем подпись и клавиатуру к последнему элементу
                media_group[-1].caption = text
                media_group[-1].parse_mode = self.parse_mode

                sent_msg = await message.reply_media_group(
                    media=media_group,
                    disable_notification=self.disable_notification,
                    protect_content=self.protect,
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
                        action=ChatAction.UPLOAD_DOCUMENT,
                    )
            else:
                # Одиночное медиа или другие типы
                for idx, media_path in enumerate(self.path_to_media):
                    is_last = idx == len(self.path_to_media) - 1
                    url = valid_url(media_path)

                    if self.media == "photo":
                        if url:
                            sent_msg = await message.reply_photo(
                                photo=media_path,
                                caption=text if is_last else None,
                                reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                parse_mode=self.parse_mode,
                                disable_notification=self.disable_notification,
                                protect_content=self.protect,
                            )
                        else:
                            sent_msg = await message.reply_photo(
                                photo=types.FSInputFile(path=media_path),
                                caption=text if is_last else None,
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
                            sent_msg = await message.reply_animation(
                                animation=media_path,
                                caption=text if is_last else None,
                                reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                parse_mode=self.parse_mode,
                                disable_notification=self.disable_notification,
                                protect_content=self.protect,
                            )
                        else:
                            sent_msg = await message.reply_animation(
                                animation=types.FSInputFile(path=media_path),
                                caption=text if is_last else None,
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
                            sent_msg = await message.reply_video(
                                video=media_path,
                                caption=text if is_last else None,
                                reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                parse_mode=self.parse_mode,
                                disable_notification=self.disable_notification,
                                protect_content=self.protect,
                            )
                        else:
                            sent_msg = await message.reply_video(
                                video=types.FSInputFile(path=media_path),
                                caption=text if is_last else None,
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
                            sent_msg = await message.reply_video_note(
                                video_note=media_path,
                                caption=text if is_last else None,
                                reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                parse_mode=self.parse_mode,
                                disable_notification=self.disable_notification,
                                protect_content=self.protect,
                            )
                        else:
                            sent_msg = await message.reply_video_note(
                                video_note=types.FSInputFile(path=media_path),
                                caption=text if is_last else None,
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
                            sent_msg = await message.reply_audio(
                                audio=media_path,
                                caption=text if is_last else None,
                                reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                parse_mode=self.parse_mode,
                                disable_notificatioввn=self.disable_notification,
                                protect_content=self.protect,
                            )
                        else:
                            sent_msg = await message.reply_audio(
                                audio=types.FSInputFile(path=media_path),
                                caption=text if is_last else None,
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
                            sent_msg = await message.reply_document(
                                document=media_path,
                                caption=text if is_last else None,
                                reply_markup=self.keyboard() if is_last and self.keyboard else None,
                                parse_mode=self.parse_mode,
                                disable_notification=self.disable_notification,
                                protect_content=self.protect,
                            )
                        else:
                            sent_msg = await message.reply_document(
                                document=types.FSInputFile(path=media_path),
                                caption=text if is_last else None,
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
                        sent_msg = await message.reply_dice(
                            emoji="🎲",  # Эмодзи кубика как стандартное значение, если нет URL
                            caption=text if is_last else None,
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

                    # Сохраняем идентификатор последнего сообщения, если необходимо
                    if sent_msg:
                        self.last_bot_message[message.chat.id] = sent_msg.message_id

                    if self.delete_msg:
                        await message.bot.delete_message(
                            chat_id=message.chat.id,
                            message_id=message.message_id
                        )

        # Проверка на ошибку
        except Exception as e:
            Logs.error(log_type=self.log_type, user=username(message), text=f"Ошибка команды: {e}")
