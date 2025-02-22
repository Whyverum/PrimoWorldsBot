# BotLibrary/system/bots.py
# Создание и настройка бота в одном файле

from aiogram import Dispatcher, Bot, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from ..timer import *
from ProjectsFiles import *

# Создание экземпляра диспатчера, строителей кнопок
dp = Dispatcher()
rkb = ReplyKeyboardBuilder()
ikb = InlineKeyboardBuilder()


# Настройка параметров диспатчера
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


# Объявление экземпляров и переменных
bot_properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML,  # Устанавливаем формат HTML для всех сообщений
    disable_notification=True,  # Отключаем уведомления при отправке сообщений
    protect_content=True,  # Защищаем содержимое сообщений от копирования
    allow_sending_without_reply=True,  # Разрешаем отправлять сообщения без ответа на другое сообщение
    link_preview_is_disabled=True,  # Отключаем предварительный просмотр ссылок
    show_caption_above_media=False,  # Показываем подпись выше медиа
)
bot = Bot(token=bot_token, default=bot_properties)     # Объявление бота
F_Media = F.photo | F.files | F.video | F.animation | F.voice | F.video_note  # Фильтр-медиа
F_All = F.text | F.photo | F.files | F.video | F.animation | F.voice | F.video_note # Фильтр на все


# Класс для хранения данных о боте (некоторые переменные даны как шаблон)
class BotInfo:
    # Статические переменные для хранения данных
    id = None
    first_name = None
    last_name = None
    username = None
    description = None
    short_description = None
    can_join_groups = None
    can_read_all_group_messages = None
    language_code = BotVar.language
    prefix = BotVar.prefix
    is_premium = None
    added_to_attachment_menu = None
    supports_inline_queries = None
    can_connect_to_business = None
    has_main_web_app = None

    # Метод для обновления данных
    @classmethod
    def update(cls, bot_info):
        cls.id = bot_info.id
        cls.first_name = bot_info.first_name
        cls.last_name = bot_info.last_name
        cls.username = bot_info.username
        cls.description = getattr(bot_info, 'description', '')
        cls.short_description = getattr(bot_info, 'description', '')
        cls.language_code = bot_info.language_code
        cls.is_premium = bot_info.is_premium
        cls.added_to_attachment_menu = bot_info.added_to_attachment_menu
        cls.supports_inline_queries = bot_info.supports_inline_queries
        cls.can_connect_to_business = bot_info.can_connect_to_business
        cls.has_main_web_app = bot_info.has_main_web_app
        cls.can_join_groups = getattr(bot_info, 'can_join_groups', None)
        cls.can_read_all_group_messages = getattr(bot_info, 'can_read_all_group_messages', None)


# Функция получения данных о боте
async def bot_get_info():
    # Получение информации о боте
    bot_info_data = await bot.get_me()

    # Обновляем данные о боте в BotInfo
    BotInfo.update(bot_info_data)

    # Возвращаем обновленные данные
    return {
        'bot_info': bot_info_data,
        'id': bot_info_data.id,
        'first_name': bot_info_data.first_name,
        'last_name': bot_info_data.last_name,
        'username': bot_info_data.username,
        'description': getattr(bot_info_data, 'description', ''),
        'short_description': getattr(bot_info_data, 'description', ''),
        'language_code': bot_info_data.language_code,
        'prefix': BotVar.prefix,
        'is_premium': bot_info_data.is_premium,
        'added_to_attachment_menu': bot_info_data.added_to_attachment_menu,
        'supports_inline_queries': bot_info_data.supports_inline_queries,
        'can_connect_to_business': bot_info_data.can_connect_to_business,
        'has_main_web_app': bot_info_data.has_main_web_app,
        'can_join_groups': getattr(bot_info_data, 'can_join_groups', None),
    }
