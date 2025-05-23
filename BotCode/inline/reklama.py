# BotCode/inline/reklama.py
# Работа с инлайн запросами на рекламу

from aiogram import Router
from aiogram.types import (InlineQueryResultPhoto, InlineQuery, CallbackQuery,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from BotLibrary import bot

# Настройка экспорта в модули
router = Router(name="reklama_inline_router")
image_url = "https://cdn.tripster.ru/photos/0bc3afa7-3847-4b47-aaf1-60202f48fb2a.jpg"  # URL изображения
text_msg = \
f"""Это сообщение с изображением и инлайн кнопками!
""" + "#флуд #ролевая #геншинимпакт #геншин #flood #rp #genshin"


@router.callback_query(lambda c: c.data == 'button_1')
async def process_callback_button(callback_query: CallbackQuery) -> None:
    await bot.answer_callback_query(callback_query.id, text="Вы нажали первую кнопку!")
    await bot.send_message(callback_query.from_user.id, "Ответ на вашу кнопку.")


@router.inline_query()
async def inline_echo(inline_query: InlineQuery) -> None:
    # Содержимое запроса
    query = inline_query.query

    # Подготавливаем результат для ответа
    if query:
        # Отправляем заготовленное сообщение с инлайн кнопками
        result_id = inline_query.id  # уникальный ID для запроса

        # Создаем инлайн результат с изображением
        items = [
            InlineQueryResultPhoto(
                id=result_id,
                photo_url=image_url,  # URL изображения
                thumbnail_url=image_url,  # Миниатюра изображения
                caption=text_msg,  # Текст, который будет показываться под изображением
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(text="Посмотреть инфо-канал", url="https://t.me/adeptusfiziks")],
                        [InlineKeyboardButton(text="Вторая кнопка", callback_data="button_1")],
                    ]
                )
            )
        ]
        # Отправляем результат в инлайн режиме
        await bot.answer_inline_query(inline_query.id, items)
