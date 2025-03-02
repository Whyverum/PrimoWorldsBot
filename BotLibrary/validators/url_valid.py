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
def url_to_text(text: str = "Тест", url: str = "www.google.com") -> str:
    return f'<b><a href="{url}">{text}</a></b>'
