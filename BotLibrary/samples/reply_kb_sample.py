# BotCode/keyboards/reply_kb/base_reply_kb.py
# Базовый класс для создания reply-клавиатур

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, WebAppInfo, KeyboardButtonRequestUsers, KeyboardButtonRequestChat, KeyboardButtonRequestUser
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from typing import List, Union, Tuple, Optional, Dict, Any

# Настройка экспорта в модули
__all__ = ("BaseReplyKeyboard",)

class BaseReplyKeyboard:
    def __init__(
            self,
            buttons: List[List[Union[str, Tuple[str, str, Optional[Dict[str, Any]]]]]],
            resize_keyboard: bool = True,
            one_time_keyboard: bool = False,
            row_width: int = 1  # Добавляем row_width как параметр
    ):
        """
        :param buttons: список кнопок, каждая из которых может быть:
                        - строкой (обычная кнопка с текстом)
                        - кортежем (текст, тип кнопки, дополнительные параметры).
                        Типы кнопок: "location", "contact", "users", "chat", "poll", "quiz", "web_app", "user".
                        Дополнительные параметры: словарь с настройками (опционально).
        :param resize_keyboard: изменять ли размер клавиатуры под содержимое.
        :param one_time_keyboard: скрывать ли клавиатуру после нажатия.
        :param row_width: количество кнопок в одной строке (если требуется динамическое распределение).
        """
        self.buttons = buttons
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.row_width = row_width

    def get_keyboard(self) -> ReplyKeyboardMarkup:
        """
        Создаёт reply-клавиатуру с поддержкой всех типов кнопок и динамическим распределением по row_width.
        :return: объект ReplyKeyboardMarkup
        """
        rkb = ReplyKeyboardBuilder()

        # Преобразуем вложенные списки в плоский список для динамического распределения
        flat_buttons = [button for row in self.buttons for button in row]

        # Разбиваем кнопки на строки с учетом row_width
        for i in range(0, len(flat_buttons), self.row_width):
            row = flat_buttons[i:i + self.row_width]
            buttons = []
            for button in row:
                if isinstance(button, tuple):
                    text, button_type = button[0], button[1]
                    params = button[2] if len(button) > 2 else {}

                    if button_type == "location":
                        buttons.append(KeyboardButton(text=text, request_location=True))
                    elif button_type == "contact":
                        buttons.append(KeyboardButton(text=text, request_contact=True))
                    elif button_type == "users":
                        buttons.append(KeyboardButton(
                            text=text,
                            request_users=KeyboardButtonRequestUsers(
                                request_id=params.get("request_id", 1),
                                user_is_bot=params.get("user_is_bot"),
                                user_is_premium=params.get("user_is_premium"),
                                max_quantity=params.get("max_quantity", 1)
                            )
                        ))
                    elif button_type == "chat":
                        buttons.append(KeyboardButton(
                            text=text,
                            request_chat=KeyboardButtonRequestChat(
                                request_id=params.get("request_id", 1),
                                chat_is_channel=params.get("chat_is_channel", False),
                                chat_is_forum=params.get("chat_is_forum"),
                                chat_has_username=params.get("chat_has_username"),
                                chat_is_created=params.get("chat_is_created")
                            )
                        ))
                    elif button_type == "poll":
                        buttons.append(KeyboardButton(
                            text=text,
                            request_poll=KeyboardButtonPollType(type="regular")
                        ))
                    elif button_type == "quiz":
                        buttons.append(KeyboardButton(
                            text=text,
                            request_poll=KeyboardButtonPollType(type="quiz")
                        ))
                    elif button_type == "web_app":
                        buttons.append(KeyboardButton(
                            text=text,
                            web_app=WebAppInfo(url=params.get("url", ""))
                        ))
                    elif button_type == "user":
                        buttons.append(KeyboardButton(
                            text=text,
                            request_user=KeyboardButtonRequestUser(
                                request_id=params.get("request_id", 1),
                                user_is_bot=params.get("user_is_bot"),
                                user_is_premium=params.get("user_is_premium")
                            )
                        ))
                else:
                    buttons.append(KeyboardButton(text=button))
            rkb.row(*buttons)

        return rkb.as_markup(resize_keyboard=self.resize_keyboard, one_time_keyboard=self.one_time_keyboard)
