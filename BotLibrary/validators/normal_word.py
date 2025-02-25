# BotLibrary/validators/normal_word.py
# Нормализирует вид слова автоматически

async def normal_words(word : str = "Тестовое слово") -> str:
    return word.lower().capitalize()
