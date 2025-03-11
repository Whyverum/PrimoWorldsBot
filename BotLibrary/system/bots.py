# BotLibrary/system/bots.py
# Создание и настройка бота в одном файле

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
dp["started_at_msk"] = get_city_time()
dp["is_active"] = True  # Флаг активности бота
dp["logs"] = []
dp["users"] = {}
dp["sessions"] = {}
dp["task_queue"] = []
dp["configs"] = {"max_connections": 100, "retry_interval": 5, "time_format": BotVar.time_format}
dp["metrics"] = {"messages_received": 0, "messages_sent": 0, "errors": 0}
dp["modules"] = {}
dp["state"] = {}
dp["scheduler"] = []
dp["handlers"] = {"on_message": [], "on_error": []}
dp["storage"] = {}
dp["database"] = None

# Настройки для бота
bot_properties = DefaultBotProperties(
    parse_mode=BotVar.parse_mode,
    disable_notification=BotVar.disable_notification,
    protect_content=BotVar.protect_content,
    allow_sending_without_reply=BotVar.allow_sending_without_reply,
    link_preview_is_disabled=BotVar.link_preview_is_disabled,
    link_preview_prefer_small_media=BotVar.link_preview_prefer_small_media,
    link_preview_prefer_large_media=BotVar.link_preview_prefer_large_media,
    link_preview_show_above_text=BotVar.link_preview_show_above_text,
    show_caption_above_media=BotVar.show_caption_above_media,
)

# Создание экземпляра бота
bot = Bot(token=bot_token, default=bot_properties)

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
    bot_owner: str = BotVar
    last_name: str = None
    username: str = None
    description: str = None
    short_description: str = None
    can_join_groups: bool = False
    can_read_all_group_messages: bool = False
    language_code: str = BotVar.language
    prefix: str = BotVar.prefix
    is_premium: bool = False
    added_to_attachment_menu: bool = False
    supports_inline_queries: bool = False
    can_connect_to_business: bool = False
    has_main_web_app: bool = False

    @classmethod
    def update(cls, bot_info) -> None:
        """
        Обновляет данные о боте.
        :param bot_info: Объект с данными о боте, полученные через API Telegram.
        """
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

async def bot_get_info() -> dict:
    """
    Получает информацию о боте и обновляет данные в классе BotInfo.
    :return: Словарь с данными о боте.
    """
    bot_info_data = await bot.get_me()
    BotInfo.update(bot_info_data)
    return {
        'bot_info': bot_info_data,
        'id': bot_info_data.id,
        'first_name': bot_info_data.first_name,
        'last_name': bot_info_data.last_name,
        'username': bot_info_data.username,
        'description': getattr(bot_info_data, 'description', ''),
        'short_description': getattr(bot_info_data, 'short_description', ''),
        'language_code': bot_info_data.language_code,
        'prefix': BotVar.prefix,
        'is_premium': bot_info_data.is_premium,
        'added_to_attachment_menu': bot_info_data.added_to_attachment_menu,
        'supports_inline_queries': bot_info_data.supports_inline_queries,
        'can_connect_to_business': bot_info_data.can_connect_to_business,
        'has_main_web_app': bot_info_data.has_main_web_app,
        'can_join_groups': getattr(bot_info_data, 'can_join_groups', False),
        'can_read_all_group_messages': getattr(bot_info_data, 'can_read_all_group_messages', False),
    }
