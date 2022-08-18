from urllib import request
import requests
from conf import token_weather

def get_weather(city, token_weather):
    icon_cod = {
        'clear sky': 'Ясно',
        'few clouds': 'Небольшая облачность',
        'scattered clouds': 'Незначительная облака',
        'broken clouds': 'Знаяительная облачность',
        'shower rain': 'Ливень',
        'rain': 'Дождь',
        'thunderstorm': 'Шторм',
        'snow': 'Снег',
        'mist': 'Туман',
    }
    try:
        req_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric')
        req_weather = req_weather.json()
        city = req_weather['name']
        temp = req_weather['main']['temp']
        vlag = req_weather['main']['humidity']
        davl = req_weather['main']['pressure']
        wind = req_weather['wind']['speed']
        icon = req_weather['weather'][0]['description']
        weather_des = req_weather['weather'][0]['description']
        if weather_des in icon_cod:
            wd = icon_cod[weather_des]
        else:
            wd = ""
        res = f'Погода в городе: {city}\nТемпература: {temp} C, {wd}\nВлажность: {vlag} %\nДавление: {davl} мм.рт.ст.\nСкорость ветра: {wind} м/с'
        return res
        # print(f'Погода в городе: {city}\n'
        #         f'Температура: {temp} C, {wd}\n'
        #         f'Влажность: {vlag} %\n'
        #         f'Давление: {davl} мм.рт.ст.\n'
        #         f'Скорость ветра: {wind} м/с')
    except Exception as i:
        print(i)