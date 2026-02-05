# no_gif -  Декоратор для повторных попыток получения не-GIF изображения и такой же для кинопоиска
import requests
from requests import Response

from api.utils import skip_gif
from log import function_logs


@function_logs
@skip_gif()
def get_random_cat() -> str:
    """
    Функция для получения ссылки на фотографию рандомного кота.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    response: Response = requests.get(url=url)
    cat_url: str = response.json()[0]['url']

    return cat_url


if __name__ == '__main__':
    get_random_cat()
