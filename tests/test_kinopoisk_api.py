from random import choices
from string import ascii_letters
from typing import List

import unittest

from api import Kinopoisk


class TestKinopoiskApi(unittest.TestCase):
    """Класс тестирующий модуль по работе с сервисом 'Kinopoisk'. """

    @classmethod
    def setUpClass(cls) -> None:
        """Создание обьекта модуля для всех тестов"""
        cls.kinopoisk = Kinopoisk()

    def test_film_funcs_is_dict(self) -> None:
        """Проверка что поиск фильма по имени возвращает словарь"""
        film_by_name = self.kinopoisk.get_film_by_name(name="Анора")
        film_random = self.kinopoisk.get_random_film()

        self.assertIsInstance(film_by_name, dict)
        self.assertIsInstance(film_random, dict)

    def test_film_keys(self) -> None:
        """Проверят что функци получения фильма возвращает ожидаемые ключи из instanse.film_keys """
        film_keys: List[str] = ["name", "description", "year", "poster"]

        film_by_name = self.kinopoisk.get_film_by_name(name="Анора")
        film_random = self.kinopoisk.get_random_film()
        film_by_name_keys: List[str] = [film_key for film_key in film_by_name.keys()]
        film_random_keys = [film_key for film_key in film_random .keys()]

        self.assertListEqual(film_keys, film_by_name_keys)
        self.assertListEqual(film_keys, film_random_keys)

    def test_get_film_by_wrong_name(self) -> None:
        """Тест проверяющий, что возвращается словарь с ошибкой о том, что фильм не найден"""
        wrong_name = "".join(choices(ascii_letters, k=10))
        result = self.kinopoisk.get_film_by_name(name=wrong_name)

        self.assertIsInstance(result, dict)
        self.assertIn("message", result)
        self.assertIn(wrong_name, result["message"])
        self.assertIn("не найден", result["message"])

    def test_randon_film_is_not_none(self) -> None:
        """Тест: проверка на то, что рандомный фильм не имеет значений None или пустую строку"""
        film = self.kinopoisk.get_random_film()
        film_value_list = [film_value for film_value in film.values()]

        self.assertNotIn(None, film_value_list)
        self.assertNotIn("", film_value_list)
