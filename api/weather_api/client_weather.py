from typing import Any, Dict

import requests

from config import WEATHER_API


class WeatherApi:
    """
    Класс предорставляюбщий интерефес по получению информации о погоде
    """
    BASE_URL = "http://api.weatherapi.com/v1"

    def today_weather(self, city: str) -> Dict[str, Any]:
        """
        Функция для получения текущей погоды в выбранном городе

        :param city: город в котором требуется определить погоду
        :return: словарь с набором данных
        """
        url = f"{self.BASE_URL}/current.json"
        params = {"q": city,
                  "key": WEATHER_API}

        response = requests.get(url=url, params=params)
        result_data = response.json()

        if "error" in result_data:
            return result_data

        weather_data = self._today_data(default_data=response.json())

        return weather_data

    def tomorow_weather(self, city: str) -> Dict[str, Any] :
        """
        Функция для получения текущей погоды в выбранном городе  на завтра

        :param city: город в котором требуется определить погоду
        :return: словарь с набором данных
        """

        url = f"{self.BASE_URL}/forecast.json"
        params = {"q": city,
                  "key": WEATHER_API,
                  "days": 2}

        response = requests.get(url=url, params=params)
        result_data = response.json()

        if "error" in result_data:
            return result_data

        tomorrow_data = result_data['forecast']['forecastday'][1]
        weather_data = self._tomorrow_data(default_data=tomorrow_data)

        return weather_data

    def _date_reformat(self, date: str) -> str:
        """
        Функция для преобразования даты из вида гггг-мм-дд в дд.мм.гггг
        :param date: изначальная дата
        :return: преобразованная дата
        """
        date_list = date.split("-")
        date_list.reverse()
        reformated_date = ".".join(date_list)

        return reformated_date

    def _tomorrow_data(self, default_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Функция для сбора определенных - средних данных из всех полученных данных о погоде из API

        :param default_data: исходный словарь
        :return: кастомный словарь с данным:
            1 описание погоды
            2 иконка
            3 максимальная скорость ветра в км/ч
            4 градусы

        """
        day = self._date_reformat(date=default_data['date'])
        weather_descr: str = default_data['day']['condition']['text']
        icon: str = default_data['day']['condition']['icon']
        wind_speed: int = default_data['day']["maxwind_kph"]
        temperature: int = default_data['day']["avgtemp_c"]

        weather_dict = {
            "day": day,
            "weather": weather_descr,
            'icon': icon,
            'wind_speed': wind_speed,
            'temperature': temperature,
        }

        return weather_dict

    def _today_data(self, default_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Функция для сбора определенных данных из всех полученных данных о погоде из API

        :param default_data: исходный словарь
        :return: кастомный словарь с данным:
            1 описание погоды
            2 иконка
            3 ветер в км/ч
            4 градусы
            5 градусы 'по ощущениям'
        """
        weather_descr: str = default_data['current']['condition']['text']
        icon: str = default_data['current']['condition']['icon']
        wind_speed: int = default_data['current']['wind_kph']
        temperature: int = default_data['current']['temp_c']
        temp_feels_like: int = default_data['current']['feelslike_c']

        weather_dict = {
            "weather": weather_descr,
            'icon': icon,
            'wind_speed': wind_speed,
            'temperature': temperature,
            'temp_feels_like': temp_feels_like
        }

        return weather_dict

    def _display_info(self, weather_data: Dict[str, Any]) -> None:
        """Функция для отображдения в консоли данных о погоде"""

        print("=" * 30, "WEATHER INFO", "=" * 30, )
        for weather_key, weather_value in weather_data.items():
            print(f"\t{weather_key} - {weather_value}")
        print("=" * 72)


if __name__ == '__main__':
    weather = WeatherApi()
    print(weather.today_weather(city="Dmitrov"))
    print(weather.tomorow_weather(city="Dmitrov"))
