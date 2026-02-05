"""Декораторы для логирования"""
import functools
import time
from dataclasses import dataclass
from typing import Any, Callable

from log import logger
from .utils import _args_to_str, _kwargs_to_str


def class_logs(cls):
    """
    Декоратор класса, который логирует все методы.
    Не принимает параметров - использует function_logs внутри.

    Args:
        cls: Класс для декорирования

    Returns:
        Класс с залогированными методами
    """
    for attr_name in dir(cls):
        attr_value = getattr(cls, attr_name)

        if (callable(attr_value) and
                not attr_name.startswith('__') and
                not attr_name.startswith('_')):
            decorated_method = function_logs(attr_value)
            setattr(cls, attr_name, decorated_method)

    return cls


def function_logs(func: Callable) -> Callable:
    """Декоратор логирующий вызов функции и ее параметры"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        log_args = _args_to_str(arguments=args)
        log_kwargs = _kwargs_to_str(keyword_args=kwargs)
        coma = ", " if args and kwargs else ""

        logger.info(f"Вызов функции {func.__name__}")
        logger.debug(f"Функция: {func.__name__}({log_args}{coma}{log_kwargs})")
        logger.debug(f"Документация: \t{func.__doc__}")

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        result_time = end_time - start_time

        if result:
            logger.debug(f"Ответ функции: {func.__name__} = {result}")

        logger.info(f"Завершение функции: {func.__name__}. (Время работы функции: {result_time:.6f})")

        return result
    return wrapper


@function_logs
def test_sum_a_b(num_a: int, num_b: int) -> int:
    """
    Функция сложение
    :param num_a: первое число для сложения
    :param num_b: второе число для сложения
    :return: сумма двух чисел
    """
    return num_a + num_b

@class_logs
@dataclass
class TestClass:

    def test(self, *args, **kwargs):
        """Тестовая функция test"""
        return "test"


if __name__ == '__main__':
    # test_sum_a_b(num_a = 1, num_b=2, )
    test = TestClass()
    test.test(1, 2, name=12, a =2)