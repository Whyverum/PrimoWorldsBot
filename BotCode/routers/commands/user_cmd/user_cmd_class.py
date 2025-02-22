# BotCode/routers/commands/user_cmd_class.py
# Класс-шаблон для создания новых команд

from aiogram import Router, types
from aiogram.filters import Command
from BotLibrary import *

# Класс-шаблон для команд
class CommandHandler:
    def __init__(self, name: str, keywords : list,
                 description: str = "Описание команды", text_msg : str = "Сообщение",
                 keyboard = None, prefix = BotVar.prefix,
                 ignore_case : bool = True, activate_keywoards : bool = True,
                 activate_commands : bool = True,
                 ):
        """
        Универсальный обработчик команд для бота.

        :param name: Имя команды (например, "help").
        :param description: Описание команды.
        :param keywords: Список ключевых слов, которые активируют команду.
        :param text_msg: Текст сообщения, который отправляется пользователю.
        :param keyboard: Клавиатура, если требуется.
        """
        self.router = Router(name=f"{name}_router")
        self.name = name
        self.log_type = name.capitalize()
        self.description = description
        self.keywords = keywords
        self.text_msg = text_msg
        self.keyboard = keyboard

        # Привязываем хэндлер к роутеру
        if activate_commands:
            self.router.message(Command(*keywords, prefix=prefix, ignore_case=ignore_case))(self.handler)
        if activate_keywoards:
            self.router.message(F.text.lower().in_(keywords))(self.handler)


    async def handler(self, message: types.Message):
        """Основной хэндлер команды."""
        user = f"@{message.from_user.username or message.from_user.id}"
        try:
            logger.bind(log_type=self.name.capitalize(), user=user).info(f"использовал(а) команду /{self.name}")
            await message.reply(
                text=self.text_msg,
                reply_markup=self.keyboard() if self.keyboard else None,
            )

        # Проверка на ошибку
        except Exception as e:
            logger.bind(log_type=self.name.capitalize(), user=user).error(f"Ошибка команды: {e}")
