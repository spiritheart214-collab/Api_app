import requests
from requests import Response

from api import get_random_cat


class TestCatApiRandomCat:
    """
    Класс тестирующий функцию get_random_cat_url для получения рандомного кота
    """
    def test_get_cat_is_str(self) -> None:
        """Функция тестируюшая тип данных ответа на соответствие типу str"""
        result = get_random_cat()

        assert isinstance(result, str), f"Ответ функции не является строкой"

    def test_get_cat_is_url(self):
        """Функция проверяющая, что ответ является ссылкой"""
        result: str = get_random_cat()

        is_url: bool = True if result.startswith('https://') or result.startswith('http://') else False

        assert is_url, "Ответ не является ссылкой"

    def test_cat_in_url(self) -> None:
        """Функция тестируюшая наличие слова cat в адресной строке"""
        result = get_random_cat()

        has_cat = "cat" in result
        assert has_cat, f"Слово 'cat' не найдено в: {result}"

    def test_no_gif_in_url(self) -> None:
        """Проверяет, что функция не возвращает .gif URL"""
        for attempt in range(10):
            url = get_random_cat()
            assert '.gif' not in url.lower(), f"Найден .gif в URL #{attempt + 1}: {url}"

    def test_status_code_200(self) -> None:
        """Функция тестируюшая статус код - 200"""
        result = get_random_cat()
        response: Response = requests.get(url=result)

        assert response.status_code == 200, "Ответ не соответсвует коду 200"
