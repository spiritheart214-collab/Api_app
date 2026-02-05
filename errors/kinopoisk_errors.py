class KinopoiskError(Exception):
    """Базовое исключение для ошибок Kinopoisk API"""
    def __init__(self, message: str):
        super().__init__(message)


class MovieNotFoundError(KinopoiskError):
    """Исключение, когда фильм не найден"""
    def __init__(self, movie_name: str) -> None:
        message = f"Фильм с именем '{movie_name}' не найден"
        super().__init__(message)
