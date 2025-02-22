# BotLibrary/loggers/start_info_out.py
# Вывод данных бота в консоль для начальной проверки

from time import sleep
from colorama import Fore

from ProjectsFiles import Permissions
from .logs import logger
from ..system import BotInfo


# Функция для получения информации о боте и выводе ее в консоль и файл
def bot_info_out():
    try:
        bot_name = f"Основное имя: {BotInfo.first_name}\n"
        bot_post_name = f" Доп. имя: {BotInfo.last_name}\n"
        bot_username = f" Юзернейм: @{BotInfo.username}\n"
        bot_id = f" ID: {BotInfo.id}\n"
        bot_language = f" Языковой код: {BotInfo.language_code}\n"
        bot_can_join_groups = f" Может ли вступать в группы: {BotInfo.can_join_groups}\n"
        bot_can_read_all_group_messages = f" Чтение всех сообщений: {BotInfo.can_read_all_group_messages}\n"
        bot_is_premium = f" Является премиум-ботом: {BotInfo.is_premium}\n"
        bot_added_to_attachment_menu = f" Добавлен в меню вложений: {BotInfo.added_to_attachment_menu}\n"
        bot_supports_inline_queries = f" Поддерживает инлайн-запросы: {BotInfo.supports_inline_queries}\n"
        bot_can_connect_to_business = f" Подключение к бизнес-аккаунтам: {BotInfo.can_connect_to_business}\n"
        bot_has_main_web_app = f" Основное веб-приложение: {BotInfo.has_main_web_app}\n"

        # Формируем полный текст с выводом информации о боте
        bot_all_info = (f"{bot_name} {bot_post_name} {bot_username} {bot_id} {bot_language} "
                        f"{bot_can_join_groups} {bot_can_read_all_group_messages} {bot_is_premium} "
                        f"{bot_added_to_attachment_menu} {bot_supports_inline_queries} {bot_can_connect_to_business} "
                        f"{bot_has_main_web_app}")

        # Печатаем все данные в консоль с задержкой в 1 секунду
        sleep(1)
        if Permissions.start_info_console:
            print(Fore.CYAN + bot_all_info)

        return bot_all_info

    # Проверка на ошибку и ее логирование
    except Exception as e:
        logger.bind(log_type="INFO", user="Start_INFO").error(f"Ошибка при получении ID пользователя: {e}")
