import aiohttp
from ProjectsFiles import weather_api_key


async def get_weather(message, *args) -> str:
    # Извлекаем город из сообщения
    command_parts = message.text.split(maxsplit=1)
    print(command_parts[1])
    if len(command_parts) > 1:
        city = command_parts[1]
    else:
        return "Пожалуйста, укажите город."

    # Обработка города
    city = city.lower().capitalize()

    # URL для запроса к API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=ru"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

        if data["cod"] != 200:
            return "Город не найден. Попробуйте еще раз."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        weather_today: str = (f"Погода <b>{city}</b>\n"
                     f"☁️Погода: <b>{weather}</b>\n"
                     f"🌡Температура: <b>{temp}°C</b>\n"
                     f"💧Влажность: <b>{humidity}%</b>\n"
                     f"💨Скорость ветра: <b>{wind} м/с</b>")
        await message.answer(weather_today)
        return weather_today
    except Exception as e:
        return f"Произошла ошибка при получении данных о погоде: {str(e)}"
