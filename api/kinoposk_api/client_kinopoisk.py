from typing import Dict, Optional, Union

import requests

from api.utils import skip_incompolete
from config import KINOPOISK_API
from errors import MovieNotFoundError
from log import class_logs


@class_logs
class Kinopoisk:
    """Класс описывает взаимодейтсвие с сервисом кинопоиск"""

    _BASE_URL = "https://api.poiskkino.dev"
    _HEADERS = {"X-API-KEY": KINOPOISK_API}

    @skip_incompolete
    def get_random_film(self) -> Dict[str, Union[str, int]]:
        """Функция получения рандомного фильма."""
        url = f"{self._BASE_URL}/v1.4/movie/random"

        film_data: dict = requests.get(url=url, headers=self._HEADERS).json()

        custom_film_data = self._process_film_info(film_data=film_data)

        return custom_film_data

    @staticmethod
    def _process_film_info(film_data: dict) -> Dict[str, Optional[Union[str, int]]]:
        """
        Вспомогательная функция. Из словаря данных о фильме формирует свой словарь данных
        :param film_data: оригинальный словарь данных
        :return: кастомный словарь с данными: имя, описание, год, постер
        """
        name = film_data.get("name") if film_data.get("name") is not None else film_data.get('alternativeName')
        description = film_data.get('description')
        year = film_data.get("year")
        poster_data = film_data.get('poster')

        # Если постер словарь, забрать строку из словаря
        if isinstance(poster_data, str):
            poster = poster_data
        elif isinstance(poster_data, dict) and 'url' in poster_data:
            poster = poster_data.get("url")
        else:
            poster = None

        custom_film_data = {
            "name": name,
            "description": description,
            "year": year,
            "poster": poster
        }

        return custom_film_data

    def get_film_by_name(self, name: str) -> Dict[str, Union[str, int]]:
        """Функция получения фильма по названию """

        url = f"{self._BASE_URL}/v1.4/movie/search"
        params = {"query": name}

        film_data = requests.get(url=url, headers=self._HEADERS, params=params).json()

        try:
            # Если ответ пустой (0) - фильм не найден
            if len(film_data["docs"]) == 0:
                raise MovieNotFoundError(movie_name=name)

        except MovieNotFoundError as film_error:
            error_message = {"message": str(film_error)}
            return error_message

        custom_film_data = self._process_film_info(film_data=film_data["docs"][0])

        return custom_film_data


if __name__ == '__main__':
    kinopoisk = Kinopoisk()
    kinopoisk.get_random_film()
    # print(kinopoisk.get_film_by_name("Бэs hgj"))
