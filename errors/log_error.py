from typing import Any
"""
Модуль кастомных ошибок для логирования
"""


class LoggingError(Exception):
    """Базовый класс для всех ошибок логирования."""
    pass

class FormatTypeIsNotStringError(LoggingError):
    """Ошибка: переданный формат шаблона не строка"""
    def __init__(self, value: Any = None, message: str = "Шаблон логов должен быть строкой"):
        """Базовая настрорйка"""
        if value is None:
            super().__init__(message)
        else:
            value_type = type(value).__name__
            message = f"Шаблон логов должен быть строкой, получен {value_type!r} с значением {value!r}".format()
            super().__init__(message)


class IMGNotFoundExaptions(LoggingError):
    """Ошибка: не найден формат фотографии png/jpg/jpeg"""
    def __init__(self, message: str = "Не найден формат фотографии: png/jpg") -> None:
        super().__init__(message)
