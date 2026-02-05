import os

from dotenv import load_dotenv


load_dotenv()

CAT_API = os.getenv("CAT_API")
DOG_API = os.getenv("DOG_API ")
KINOPOISK_API = os.getenv("KINOPOISK_API")
WEATHER_API = os.getenv("WEATHER_API")

LOG_LEVEL = "DEBUG"
