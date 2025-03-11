# BotLibrary/validators/email_validators.py
# Создание валидации почты для проекта

from typing import Optional
from email_validator import validate_email, EmailNotValidError

# Настройка экспорта из этого модуля
__all__ = ("valid_email",)


# Функция проверки почты на корректность
def valid_email(email: str) -> Optional[str]:
    """
    Делает почтовый адрес корректным.

    :param email: Почтовый адрес в виде строки.
    :return: Нормализованный почтовый адрес, если он валиден, иначе None.
    """
    try:
        return validate_email(email).normalized
    except EmailNotValidError as e:
        # Импортируем Logs внутри функции, чтобы избежать циклического импорта
        from ..loggers.custom_loggers import Logs
        Logs.error(text=f"Ошибка в нормализировании почты: {e}", log_type="NormalEmail")
        return None