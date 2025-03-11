# BotLibrary/validators/url_valid.py
# Валидатор ссылок на регулярных выражениях

import re

# Настройка экспорта из этого модуля
__all__ = ("valid_url", "url_to_text")


# Функция определения является ли строка ссылкой
def valid_url(url: str) -> bool:
    """
    Проверяет, является ли строка валидной ссылкой (URL).

    :param url: Строка для проверки.
    :return: True, если строка является валидным URL, иначе False.
    """
    url_pattern = re.compile(
        r'^(https?://)?'  # Протокол (http или https, необязателен)
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # Домен
        r'(:\d+)?'  # Порт (необязателен)
        r'(/[-a-zA-Z0-9@:%_+.~#?&//=]*)?$'  # Путь, параметры и фрагменты
    )
    return bool(url_pattern.match(url))


# Функция, что дает тексту ссылку на HTML
def url_to_text(text: str, url: str) -> str:
    """
    Преобразует текст в HTML ссылку с указанным URL.

    Эта функция генерирует HTML-ссылку с переданным текстом и URL, используя тег `<а>`, и делает ссылку жирной.

    :param text: Текст, который будет отображаться для ссылки.
    :param url: URL, который будет привязан к тексту.
    :return: Строка с HTML кодом для ссылки, если URL валиден.
    :raises ValueError: Если URL невалиден.
    """
    try:
        if not valid_url(url):  # Проверяем, является ли URL валидным
            raise ValueError(f"Переданный URL '{url}' невалиден.")

        # Генерация HTML-ссылки
        return f'<b><a href="{url}">{text}</a></b>'

    except ValueError as e:
        # Импортируем Logs внутри функции, чтобы избежать циклического импорта
        from ..loggers.custom_loggers import Logs
        # Логируем ошибку с использованием Logs.error, как указано
        Logs.error(text=f"Ошибка при создании ссылки: {e}", log_type="InvalidURL")
        raise e  # Перебрасываем ошибку выше для дальнейшей обработки или уведомления