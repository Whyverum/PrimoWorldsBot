# BotLibrary/validators/email_validators.py
# Создание валидации почты для проекта

from email_validator import validate_email, EmailNotValidError
from typing import Optional

# Настройка экспорта из этого модуля
__all__ = ("valid_email",)

# Функция проверки почты на корректность
def valid_email(text: str) -> Optional[str]:
    """
    Проверяет корректность почтового адреса.

    :param text: Почтовый адрес в виде строки.
    :return: Нормализованный почтовый адрес, если он валиден, иначе None.
    """
    try:
        # Проверка и нормализация email
        email = validate_email(text)
        return email.normalized
    except EmailNotValidError:
        # Если email невалиден, можно добавить логирование или обработку ошибок
        return None
