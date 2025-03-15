# BotLibrary/validators/normal_word.py
# Нормализирует вид слова автоматически

# Настройка экспорта из этого модуля
__all__ = ("normal_words",)

async def normal_words(word: str) -> str:
    """
    Делает слово корректного вида.

    :param word: Слово, которое будет приводиться к виду (Тесты).
    :return: Нормализованное слово, иначе вернуть слово.
    """
    try:
        return word.lower().capitalize()
    except Exception as e:
        # Импортируем Logs внутри функции, чтобы избежать циклического импорта
        from ..loggers.custom_loggers import Logs
        Logs.error(text=f"Ошибка в нормализировании слова: {e}", log_type="NormalWord")
        return word