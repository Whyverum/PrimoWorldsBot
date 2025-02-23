# BotLibrary/system/bots.py
# Создание и настройка бота в одном файле

from aiogram import Dispatcher, Bot, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import Bot as BotType

from ..timer import get_host_time, get_moscow_time
from ProjectsFiles import bot_token, BotVar


# Создание строителей кнопок
rkb = ReplyKeyboardBuilder()
ikb = InlineKeyboardBuilder()

# Настройка параметров диспатчера
dp = Dispatcher()
dp["started_at"] = get_host_time()
dp["started_at_msk"] = get_moscow_time()
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
    parse_mode=ParseMode.HTML,  # Устанавливаем формат HTML для всех сообщений
    disable_notification=True,  # Отключаем уведомления при отправке сообщений
    protect_content=True,  # Защищаем содержимое сообщений от копирования
    allow_sending_without_reply=True,  # Разрешаем отправлять сообщения без ответа на другое сообщение
    link_preview_is_disabled=True,  # Отключаем предварительный просмотр ссылок
    show_caption_above_media=False,  # Показываем подпись выше медиа
)

# Создание экземпляра бота
bot = Bot(token=bot_token, default=bot_properties)  # Объявление бота

# Фильтры для различных типов сообщений
F_Media = F.photo | F.files | F.video | F.animation | F.voice | F.video_note  # Фильтр для медиа
F_All = F.text | F.photo | F.files | F.video | F.animation | F.voice | F.video_note  # Фильтр на все

# Класс для хранения данных о боте
class BotInfo:
    """
    Класс для хранения данных о боте и их обновления.
    """
    # Статические переменные для хранения данных
    id: int = None
    first_name: str = None
    last_name: str = None
    username: str = None
    description: str = None
    short_description: str = None
    can_join_groups: bool = None
    can_read_all_group_messages: bool = None
    language_code: str = BotVar.language
    prefix: str = BotVar.prefix
    is_premium: bool = None
    added_to_attachment_menu: bool = None
    supports_inline_queries: bool = None
    can_connect_to_business: bool = None
    has_main_web_app: bool = None

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
        cls.can_join_groups = getattr(bot_info, 'can_join_groups', None)
        cls.can_read_all_group_messages = getattr(bot_info, 'can_read_all_group_messages', None)


async def bot_get_info() -> dict:
    """
    Получает информацию о боте и обновляет данные в классе BotInfo.

    :return: Словарь с данными о боте.
    """
    # Получение информации о боте через API
    bot_info_data = await bot.get_me()

    # Обновляем данные о боте в BotInfo
    BotInfo.update(bot_info_data)

    # Возвращаем обновленные данные о боте
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
        'can_join_groups': getattr(bot_info_data, 'can_join_groups', None),
    }
