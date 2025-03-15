# BotLibrary/loggers/custom_loggers.py
# Кастомные логгеры для проекта, с более стандартизированным использованием

from time import sleep

from aiogram import types
from colorama import Fore
from loguru import logger
from aiogram.types import Message

from BotLibrary.system.bots import BotInfo
from BotLibrary.validators.username import username
from BotLibrary.analytics.type_msg import type_msg

from ProjectsFiles import BotLogs, Permissions, ProjectPath, BotVar, bot_owner

# Настройка экспорта из модуля
__all__ = ("Logs",)


class Logs:
    """Класс для логирования с разными уровнями через loguru."""

    @staticmethod
    def start(text: str = "Логирование!",
              system: str = "PRIMO",
              log_type: str = "AEP",
              user: str = "@Console") -> None:
        """
        Логирует сообщение на уровне START.

        :param text: Сообщение для логирования.
        :param system: Тип системы логирования.
        :param log_type: Тип лога (например, "Help").
        :param user: Имя пользователя или источник вызова лога.

        :return: Вывод сообщения об старте бота
        """
        logger.bind(system=system, user=user, log_type=log_type).log("START", text)


    @staticmethod
    def debug(text: str = "Логирование!",
              system: str = "DEBUG",
              log_type: str = "Logs",
              user: str = "@Console",
              message: Message = None) -> None:
        """
        Логирует сообщение на уровне DEBUG.

        :param text: Сообщение для логирования.
        :param system: Тип системы логирования.
        :param log_type: Тип лога (например, "Help").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.

        :return: Вывод сообщения об дебаг-информации
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).debug(text)


    @staticmethod
    def info(text: str = "Логирование!",
             system: str = "PRIMO",
             log_type: str = "Logs",
             user: str = "@Console",
             message: Message = None) -> None:
        """
        Логирует сообщение на уровне INFO.

        :param text: Сообщение для логирования.
        :param system: Тип системы логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.

        :return: Вывод сообщения об некой информации
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).info(text)


    @staticmethod
    def warning(text: str = "Логирование!",
                system: str = "WARNING",
                log_type: str = "Logs",
                user: str = "@Console",
                message: Message = None) -> None:
        """
        Логирует сообщение на уровне WARNING.

        :param text: Сообщение для логирования.
        :param system: Тип системы логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.

        :return: Вывод сообщения об предупреждении
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).warning(text)


    @staticmethod
    def error(text: str = "Логирование!",
              system: str = "ERROR",
              log_type: str = "Logs",
              user: str = "@Console",
              message: Message = None) -> None:
        """
        Логирует сообщение на уровне ERROR.

        :param text: Сообщение для логирования.
        :param system: Тип системы логирования.
        :param log_type: Тип лога (например, "Logs").
        :param user: Имя пользователя или источник вызова лога.
        :param message: Сообщение от пользователя, если необходимо извлечь имя.

        :return: Вывод сообщения об ошибке
        """
        if message:
            user = username(message)
        logger.bind(system=system, log_type=log_type, user=user).error(text)


    @staticmethod
    def msg(message: types.Message,
            log_type: str = "Message",
            user: str = None,
            msg_type: str = None,
            permission: bool = BotLogs.permission) -> None:
        """
        Логирует сообщение, если оно не обработано.

        :param message: Сообщение от пользователя.
        :param log_type: Тип лога (по умолчанию "Message").
        :param permission: Разрешение на логирование (config).
        :param user: Получение пользователя (автоматически).
        :param msg_type: Получение типа сообщения (автоматически).
.
        :return: Вывод сообщения об обычном сообщении пользователя.
        """
        # Получаем айди чата
        chat_id = message.chat.id

        # Получаем username или id пользователя
        if user is None:
            user: str = f"@{message.from_user.username or message.from_user.id}"
        if msg_type is None:
            msg_type: str = type_msg(message)

        # Логирование только если разрешено
        if permission:
            # Проверка на наличие текста и его типа
            if message.text is None and msg_type not in ("Новые участники чата", "Ушедший участник чата"):
                Logs.info(log_type=log_type, user=user, text=f"Получено сообщение из ({chat_id}) : {msg_type}")
            elif message.text is not None:
                Logs.info(log_type=log_type, user=user,
                          text=f"Получено сообщение из ({chat_id}) : {message.text}")


    @staticmethod
    def console(stop_time: int = 1,
                console: bool = Permissions.start_info_console,
                file: bool = Permissions.start_info_to_file,
                path: str = ProjectPath.bot_info_log_file) -> None:
        """
        Собирает информацию о боте и выводит её в консоль, а также возвращает как строку.

        :param stop_time: Количество времени в секундах, после которых выведется информация (1 сек)
        :param console: Разрешение на внесение информации в консоль (config)
        :param file: Разрешение на внесение информации в файл (config)
        :param path: Путь до файла для сохранения информации о боте (config)

        :return: Информация о боте в виде строки.
        """
        # Собираем данные о боте
        bot_name: str = f"Основное имя: {BotInfo.first_name}\n"
        bot_post_name: str = f"Владельцы бота: {bot_owner}\n"
        bot_username: str = f"Юзернейм: @{BotInfo.username}\n"
        bot_id: str = f"ID: {BotInfo.id}\n"
        bot_can_join_groups: str = f"Может ли вступать в группы: {BotInfo.can_join_groups}\n"
        bot_can_read_all_group_messages: str = f"Чтение всех сообщений: {BotInfo.can_read_all_group_messages}\n"
        bot_supports_inline_queries: str = f"Поддерживает инлайн-запросы: {BotInfo.supports_inline_queries}\n"
        bot_can_connect_to_business: str = f"Подключение к бизнес-аккаунтам: {BotInfo.can_connect_to_business}\n"
        bot_has_main_web_app: str = f"Основное веб-приложение: {BotInfo.has_main_web_app}\n"

        # Формируем полный текст с выводом информации о боте
        bot_all_info: str = (f"{bot_name} {bot_post_name} {bot_username} {bot_id} "
                             f"{bot_can_join_groups} {bot_can_read_all_group_messages} "
                             f"{bot_supports_inline_queries} {bot_can_connect_to_business} "
                             f"{bot_has_main_web_app}")

        # Печатаем всю информацию в консоль с задержкой
        if console:
            sleep(stop_time)
            print(Fore.CYAN + bot_all_info)

        # Печатаем всю информацию в файл
        if file:
            #  Преобразуем словарь bot_all_info в строку и записываем в файл
            with open(path, 'w', encoding=BotVar.encod) as file:
                file.write(str(bot_all_info))
