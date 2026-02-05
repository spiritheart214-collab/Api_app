import unittest

from api import WeatherApi


class TestWeatherApi(unittest.TestCase):
    """Класс тестирующий API погоды"""

    @classmethod
    def setUpClass(cls) -> None:
        """Преднастройка для всего класса тестов"""
        cls.weather = WeatherApi()

    def setUp(self) -> None:
        """Преднастройка для каждого теста. Запрос """
        self.weather_today = self.weather.today_weather(city="Moscow")
        self.weather_tomorrow = self.weather.tomorow_weather(city="Moscow")

    def test_waether_funcs_returns_dict(self) -> None:
        """Тест: функции апи возвращают не пустые словари. """

        self.assertIsInstance(self.weather_tomorrow, dict, "Cегодняшняя погода не является словарем")
        self.assertIsInstance(self.weather_today, dict, "Погода на сегодня не является словарем")

        self.assertTrue(len(self.weather_today.keys()) > 0, "Словарь имеет ключи и значения")
        self.assertTrue(len(self.weather_tomorrow.keys()) > 0, "Словарь имеет ключи и значения")

    def test_wether_keys(self) -> None:
        """Тест: проверка ожидаемых ключей словаря"""
        expected_today_keys = ["weather", 'icon', 'wind_speed', 'temperature',  'temp_feels_like']
        expected_tomorrow_keys = ["day", "weather",'icon', 'wind_speed', 'temperature']

        for key in expected_today_keys:
            self.assertIn(key, self.weather_today.keys(),  f"Ключ '{key}' отсутствует в сегодняшней погоде")

        for key in expected_tomorrow_keys:
            self.assertIn(key, self.weather_tomorrow.keys(),  f"Ключ '{key}' отсутствует в погоде на завтра")

    def test_data_types(self):
        """Тест типов данных в возвращаемых словарях"""
        # Проверяем сегодняшнюю погоду
        self.assertIsInstance(self.weather_today['weather'], str)
        self.assertIsInstance(self.weather_today['icon'], str)
        self.assertIsInstance(self.weather_today['wind_speed'], (int, float))
        self.assertIsInstance(self.weather_today['temperature'], (int, float))
        self.assertIsInstance(self.weather_today['temp_feels_like'], (int, float))

        # Проверяем завтрашнюю погоду
        self.assertIsInstance(self.weather_tomorrow['day'], str)
        self.assertIsInstance(self.weather_tomorrow['weather'], str)
        self.assertIsInstance(self.weather_tomorrow['icon'], str)
        self.assertIsInstance(self.weather_tomorrow['wind_speed'], (int, float))
        self.assertIsInstance(self.weather_tomorrow['temperature'], (int, float))

    def test_invalid_city_name(self) -> None:
        """Тест обработки несуществующего города"""

        weather_today = self.weather.today_weather(city="")
        self.assertIsInstance(weather_today, dict)
        self.assertIn("error", weather_today.keys())

        weather_today = self.weather.today_weather(city="  ")
        self.assertIsInstance(weather_today, dict)
        self.assertIn("error", weather_today.keys())

        weather_today = self.weather.today_weather(city="ThisCityDoesNotExist12345")
        self.assertIsInstance(weather_today, dict)
        self.assertIn("error", weather_today.keys())


        weather_tomorrow = self.weather.tomorow_weather(city="")
        self.assertIsInstance(weather_tomorrow, dict)
        self.assertIn("error", weather_tomorrow.keys())

        weather_tomorrow = self.weather.tomorow_weather(city="  ")
        self.assertIsInstance(weather_tomorrow, dict)
        self.assertIn("error", weather_tomorrow.keys())

        weather_tomorrow = self.weather.tomorow_weather(city="ThisCityDoesNotExist12345")
        self.assertIsInstance(weather_tomorrow, dict)
        self.assertIn("error", weather_tomorrow.keys())

    def test_temperature_ranges(self):
        """Тест что температура в разумных пределах"""
        # Сегодня
        temp = self.weather_today['temperature']
        self.assertGreaterEqual(temp, -90,
                                f"Температура слишком низкая: {temp}°C")
        self.assertLessEqual(temp, 60,
                             f"Температура слишком высокая: {temp}°C")

        # Завтра
        temp_tomorrow = self.weather_tomorrow['temperature']
        self.assertGreaterEqual(temp_tomorrow, -90)
        self.assertLessEqual(temp_tomorrow, 60)
