# BotLibrary/samples/inline_kb_sample.py
# Шаблон для создания инлайн клавиатур

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List, Tuple, Optional

# Настройка экспорта в модули
__all__ = ("BaseInlineKeyboard",)

class BaseInlineKeyboard:
    def __init__(self, buttons: List[Tuple[str, Optional[str], Optional[str]]], row_width: int = 1):
        """
        :param buttons: список кнопок в формате (текст, url, callback_data).
        :param row_width: количество кнопок в строке.
        """
        self.buttons = buttons
        self.row_width = row_width

    def get_keyboard(self) -> InlineKeyboardMarkup:
        """
        Создаёт инлайн-клавиатуру и возвращает её вместе с объектом для удаления reply-клавиатуры.
        :return: кортеж InlineKeyboardMarkup
        """
        ikb = InlineKeyboardBuilder()
        for text, url, callback_data in self.buttons:
            if url:
                ikb.button(text=text, url=url)
            elif callback_data:
                ikb.button(text=text, callback_data=callback_data)

        ikb.adjust(self.row_width)
        return ikb.as_markup()
