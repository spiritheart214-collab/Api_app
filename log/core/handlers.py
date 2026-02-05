"""
Обработчик для логгер
"""
import logging

from .formatters import ColorFormatter


def get_console_handler(
        fmt: str,
        datefmt: str,
        level: int = logging.DEBUG,
        color_scheme: str = "default") -> logging.Handler:
    """
    Создает обработчик для консоли с цветами

    :param fmt: формат вывода логов
    :param datefmt: формат вывода даты в логах
    :param level: уровень логирования
    :param color_scheme: цветовя схема
    :return: обьект консольного логера
    """

    handler = logging.StreamHandler()
    handler.setLevel(level=level)

    formatter = ColorFormatter(fmt=fmt, datefmt=datefmt, color_scheme=color_scheme)
    handler.setFormatter(formatter)

    return handler
