"""Модуль с вспомогательными декоратарами"""
import functools
from typing import Callable, Dict, Optional, Union

from errors import IMGNotFoundExaptions
from log import logger


def skip_gif(_func: Optional[Callable] = None, *, max_repeat: Optional[int] = None) -> Callable:
    """Декоратор - повторяющий функцию до тех пор пока она не вернет ссылка на картинку  формате .png/.jpg/.jpeg"""

    def inner_decorator(func: Callable) -> Callable:
        """Принzятие функции для декорирования"""

        @functools.wraps(func)
        def wrapper() -> str:
            """Повторяет вызов пока не получит не-GIF"""

            if max_repeat:
                for attempt in range(max_repeat):
                    result: str = func()

                    if not result.endswith(".gif"):
                        logger.debug(f"Успешно полученно изображение на попытке {attempt + 1}")
                        return result

                    logger.debug(f"Попытка {attempt + 1}: GIF, повторяем...")

                raise IMGNotFoundExaptions(message=f"Не удалось получить не-GIF за {max_repeat} попыток")

            else:
                attempt = 0
                while True:
                    attempt += 1
                    result: str = func()

                    if not result.endswith(".gif"):
                        logger.debug(f"Успешно полученно изображение на попытке {attempt}")
                        return result

                    logger.debug(f"Попытка {attempt}: GIF, повторяем...")

        return wrapper

    if _func is None:
        return inner_decorator
    else:
        return inner_decorator(func=_func)


def skip_incompolete(func: Callable) -> Callable:
    """Декоратор проверяет данные о фильме и если словарь данных содержит None, то поторно вызывает поиск"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Dict[str, Union[str, int]]:
        """Повторяет вызов пока не получит полный словарь данных"""
        attempt: int = int()

        while True:
            attempt += 1
            result = func(*args, **kwargs)

            logger.debug(
                f"Попытка получения данных из функции {func.__name__} №{attempt}."
            )

            if None not in result.values() and "" not in result.values():
                return result

            logger.warning(
                f"Функция {func.__name__} вернула неполные данные "
                f"(попытка {attempt}): Повторный вызов..."
            )
    return wrapper
