# BotCode/routers/old_files/media_func.py
# Некоторые функции для работы с медиа-сообщениями

from re import Match
from aiogram import Router, F, types
from magic_filter import RegexpMode
from BotLibrary import *

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="media_func")


# @router.message(F.photo, ~F.caption)
async def handle_photo_wo_caption(message: types_msg.Message):
    caption = f"Простите, я не могу это увидеть. Вы можете описать что это?"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )
    return caption


# @router.message(F.photo, F.caption.contains("please"))
async def handle_photo_with_please_caption(message: types_msg.Message):
    text = f"Простите, я не могу это увидеть."
    await message.reply(text)
    return text


# @router.message(any_media_filter, ~F.caption)
async def handle_any_media_wo_caption(message: types_msg.Message):
    if message.document:
        await message.reply_document(
            document=message.document.file_id,
        )
        return f"Перессылка документа"

    elif message.video:
        await message.reply_video(
            video=message.video.file_id,
        )
        return f"Перессылка видео"

    else:
        text = f"Я не могу это увидеть."
        await message.reply(text)
        return text


# @router.message(any_media_filter, F.caption)
async def handle_any_media_w_caption(message: types_msg.Message):
    text = f"Что-то на медиа. Твой текст: {message.caption!r}"
    await message.reply(text)
    return text
