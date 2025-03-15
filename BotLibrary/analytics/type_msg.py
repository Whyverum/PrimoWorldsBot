# BotLibrary/analytics/type_msg.py
# Проверяет тип сообщения

from aiogram.types import ContentType, Message

# Настройка экспорта из модуля
__all__ = ("type_msg",)

# Функция определения типа сообщения
def type_msg(message: Message) -> str:
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
        ContentType.CHAT_BACKGROUND_SET: "Установлен фон чата",
        ContentType.UNKNOWN: "Неизвестно",
        ContentType.ANY: "Любой тип",
        ContentType.PAID_MEDIA: "Платный контент",
        ContentType.MIGRATE_TO_CHAT_ID: "Миграция в чат",
        ContentType.MIGRATE_FROM_CHAT_ID: "Миграция из чата",
        ContentType.NEW_CHAT_MEMBERS: "Новые участники чата",
        ContentType.LEFT_CHAT_MEMBER: "Ушедший участник чата",
        ContentType.NEW_CHAT_TITLE: "Новое название чата",
        ContentType.NEW_CHAT_PHOTO: "Новая фотография чата",
        ContentType.DELETE_CHAT_PHOTO: "Удаление фотографии чата",
        ContentType.GROUP_CHAT_CREATED: "Создание группового чата",
        ContentType.SUPERGROUP_CHAT_CREATED: "Создание супергруппы",
        ContentType.CHANNEL_CHAT_CREATED: "Создание канала",
        ContentType.MESSAGE_AUTO_DELETE_TIMER_CHANGED: "Изменение таймера авто-удаления сообщения",
    }

    # Получение типа сообщения
    message_type: str = message.content_type

    # Если это контакт, добавляем номер телефона
    if message_type == ContentType.CONTACT and message.contact:
        return f"{content_types.get(message_type, 'Контакт')}: {message.contact.phone_number}"

    # Возвращаем описание типа сообщения, если оно есть в словаре, иначе "Неизвестный тип"
    return content_types.get(message_type, "Неизвестный тип")
