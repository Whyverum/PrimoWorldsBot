# BotLibrary/analytics/log_type.py
# Определение типа сообщения

from aiogram.types import ContentType
from aiogram.types import Message

# Настройка экспорта из модуля
__all__ = ("types_message",)


# Функция определения типа сообщения
def types_message(message: Message) -> str:
    """
    Функция для определения типа сообщения на основе его содержимого.

    :param message: Сообщение от пользователя.
    :return: Описание типа сообщения.
    """
    # Словарь для соответствия типов сообщений
    content_types: dict = {
        ContentType.TEXT: "Текст",
        ContentType.PHOTO: "Фото",
        ContentType.STICKER: "Стикер",
        ContentType.ANIMATION: "Гиф",
        ContentType.VOICE: "Голосовое сообщение",
        ContentType.VIDEO_NOTE: "Видео-сообщение",
        ContentType.VIDEO: "Видео",
        ContentType.AUDIO: "Аудио",
        ContentType.DOCUMENT: "Документ",
        ContentType.CONTACT: "Контакт",
        ContentType.LOCATION: "Локация",
        ContentType.VENUE: "Место",
        ContentType.DICE: "Бросок кубика",
        ContentType.STORY: "История",
        ContentType.GAME: "Игра",
        ContentType.POLL: "Опрос",
        ContentType.FORUM_TOPIC_CREATED: "Создание темы на форуме",
        ContentType.FORUM_TOPIC_EDITED: "Редактирование темы форума",
        ContentType.FORUM_TOPIC_CLOSED: "Закрытие темы форума",
        ContentType.FORUM_TOPIC_REOPENED: "Открытие темы форума",
        ContentType.GENERAL_FORUM_TOPIC_HIDDEN: "Скрытие общей темы форума",
        ContentType.GENERAL_FORUM_TOPIC_UNHIDDEN: "Раскрытие общей темы форума",
        ContentType.GIVEAWAY_CREATED: "Создание розыгрыша",
        ContentType.GIVEAWAY: "Розыгрыш",
        ContentType.GIVEAWAY_WINNERS: "Победители розыгрыша",
        ContentType.GIVEAWAY_COMPLETED: "Розыгрыш завершен",
        ContentType.VIDEO_CHAT_SCHEDULED: "Запланированный видеочат",
        ContentType.VIDEO_CHAT_STARTED: "Видеочат начат",
        ContentType.VIDEO_CHAT_ENDED: "Видеочат завершен",
        ContentType.VIDEO_CHAT_PARTICIPANTS_INVITED: "Участники приглашены в видеочат",
        ContentType.PINNED_MESSAGE: "Закрепленное сообщение",
        ContentType.INVOICE: "Счет",
        ContentType.SUCCESSFUL_PAYMENT: "Успешный платеж",
        ContentType.REFUNDED_PAYMENT: "Возврат платежа",
        ContentType.USERS_SHARED: "Пользователи поделились",
        ContentType.CHAT_SHARED: "Чат был передан",
        ContentType.CONNECTED_WEBSITE: "Подключенный веб-сайт",
        ContentType.WRITE_ACCESS_ALLOWED: "Разрешение на запись",
        ContentType.PASSPORT_DATA: "Данные паспорта",
        ContentType.PROXIMITY_ALERT_TRIGGERED: "Срабатывание предупреждения о близости",
        ContentType.BOOST_ADDED: "Буст чата",
        ContentType.CHAT_BACKGROUND_SET: "Установлен фон чата"
    }

    # Проверяем тип сообщения и возвращаем описание
    if message.pinned_message:  # Закрепленное сообщение
        return content_types.get(ContentType.PINNED_MESSAGE, "Закрепленное сообщение")

    # Проверка для обычных сообщений
    for content_type, description in content_types.items():
        if getattr(message, str(content_type.value)):  # Если тип содержимого найден
            return description

    # Если сообщение не соответствует ни одному из типов
    return "Неизвестный тип"
