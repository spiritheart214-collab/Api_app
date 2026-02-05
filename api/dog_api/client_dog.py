import requests
from requests import Response

from api.utils import skip_gif
from log import function_logs


@function_logs
@skip_gif()
def get_random_dog() -> str:
    """
    Функция для получения ссылки на фотографию рандомной собаки.
    """
    url = "https://api.thedogapi.com/v1/images/search"
    response: Response = requests.get(url=url)
    dog_url: str = response.json()[0]['url']

    return dog_url


if __name__ == '__main__':
    get_random_dog()
