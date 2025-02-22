# BotLibrary/validators/email_validators.py
# Создание валидации почты для проекта

from email_validator import validate_email, EmailNotValidError

# Настройка экспорта из этого модуля
__all__ = ("valid_email",)


# Функция проверки почты на корректность
def valid_email(text: str) -> str | None:
    try:
        email = validate_email(text)
    except EmailNotValidError:
        return None
    return email.normalized