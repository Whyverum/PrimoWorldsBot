# BotLibrary/system/bots.py
# Создание и настройка бота, диспатчера и основных инструментов

from aiogram import Dispatcher, Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from ..timer import get_host_time, get_city_time
from ProjectsFiles import bot_token, BotVar

# Создание строителей кнопок
rkb = ReplyKeyboardBuilder()
ikb = InlineKeyboardBuilder()

# Настройка параметров диспатчера
dp = Dispatcher()
dp["started_at"] = get_host_time()
dp["started_at_city"] = get_city_time()
dp["is_active"] = True  # Флаг активности бота
dp["configs"] = {"max_connections": 100, "retry_interval": 5, "time_format": BotVar.time_format}
dp["metrics"] = {"messages_received": 0, "messages_sent": 0, "errors": 0}
dp["handlers"] = {"on_message": [], "on_error": []}
dp["database"] = "SQLite3"


# Создание экземпляра бота и его настройка
bot: Bot = Bot(token=bot_token, default=DefaultBotProperties(
    parse_mode=BotVar.parse_mode,
    disable_notification=BotVar.disable_notification,
    protect_content=BotVar.protect_content,
    allow_sending_without_reply=BotVar.allow_sending_without_reply,
    link_preview_is_disabled=BotVar.link_preview_is_disabled,
    link_preview_prefer_small_media=BotVar.link_preview_prefer_small_media,
    link_preview_prefer_large_media=BotVar.link_preview_prefer_large_media,
    link_preview_show_above_text=BotVar.link_preview_show_above_text,
    show_caption_above_media=BotVar.show_caption_above_media,
))

# Фильтры для различных типов сообщений
F_Media = F.photo | F.files | F.video | F.animation | F.voice | F.video_note
F_All = F.text | F.photo | F.files | F.video | F.animation | F.voice | F.video_note


# Класс для хранения данных о боте
class BotInfo:
    """
    Класс для хранения данных о боте и их обновления.
    """
    id: int = None
    first_name: str = None
    last_name: str = None
    username: str = None
    description: str = ''
    short_description: str = ''
    language_code: str = BotVar.language
    prefix: str = BotVar.prefix
    bot_owner: str = BotVar
    is_premium: bool = False
    added_to_attachment_menu: bool = False
    supports_inline_queries: bool = False
    can_connect_to_business: bool = False
    has_main_web_app: bool = False
    can_join_groups: bool = False
    can_read_all_group_messages: bool = False

    @classmethod
    async def info(cls, bots: Bot = bot) -> dict:
        """
        Получает информацию о боте через API и обновляет данные в классе.

        :param bots: Объект бота
        :return: Словарь с данными о боте
        """
        bot_info = await bots.get_me()

        cls.id = bot_info.id
        cls.first_name = bot_info.first_name
        cls.last_name = bot_info.last_name
        cls.username = bot_info.username
        cls.description = getattr(bot_info, 'description', '')
        cls.short_description = getattr(bot_info, 'short_description', '')
        cls.language_code = bot_info.language_code
        cls.is_premium = bot_info.is_premium
        cls.added_to_attachment_menu = bot_info.added_to_attachment_menu
        cls.supports_inline_queries = bot_info.supports_inline_queries
        cls.can_connect_to_business = bot_info.can_connect_to_business
        cls.has_main_web_app = bot_info.has_main_web_app
        cls.can_join_groups = getattr(bot_info, 'can_join_groups', False)
        cls.can_read_all_group_messages = getattr(bot_info, 'can_read_all_group_messages', False)

        return cls.to_dict()

    @classmethod
    def to_dict(cls) -> dict:
        """
        Возвращает текущие данные в виде словаря.
        """
        return {
            'id': cls.id,
            'first_name': cls.first_name,
            'last_name': cls.last_name,
            'username': cls.username,
            'description': cls.description,
            'short_description': cls.short_description,
            'language_code': cls.language_code,
            'prefix': cls.prefix,
            'bot_owner': cls.bot_owner,
            'is_premium': cls.is_premium,
            'added_to_attachment_menu': cls.added_to_attachment_menu,
            'supports_inline_queries': cls.supports_inline_queries,
            'can_connect_to_business': cls.can_connect_to_business,
            'has_main_web_app': cls.has_main_web_app,
            'can_join_groups': cls.can_join_groups,
            'can_read_all_group_messages': cls.can_read_all_group_messages,
        }
