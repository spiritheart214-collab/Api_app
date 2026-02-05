"""
Модуль  для работы и настройки логгеров
Предоставляет функции для создания и кэширования логгеров с консольным выводом.
"""
import logging
from typing import Dict

from .config import LOG_CONFIG
from .handlers import get_console_handler


# Кэш созданных логгеров
_LOGHGERS_CASHE: Dict[str, logging.Logger] = dict()


def get_or_create_loger(
        name: str = "log",
        level: int = LOG_CONFIG['default_level'],
        color_scheme: str = "default",
        log_format: str = LOG_CONFIG["format"],
        date_format: str = LOG_CONFIG["date_format"]) -> logging.Logger:
    """
    Получить или создать логгер

    :param name: имя логгера
    :param level: уровень логирования
    :param color_scheme: цветовя схема
    :param log_format: формат вывода логов
    :param date_format: формат вывода даты в логах
    :return: объект настроенного логера
    """
    logger_cash_key = f"{name}_{level}_{color_scheme}_{log_format}_{date_format}"

    if logger_cash_key in _LOGHGERS_CASHE:
        return _LOGHGERS_CASHE[logger_cash_key]

    logger = logging.getLogger(name=name)
    logger.setLevel(level=level)
    logger.addHandler(get_console_handler(fmt=log_format, datefmt=date_format, color_scheme=color_scheme))

    # Кэшируем логгер
    _LOGHGERS_CASHE[logger_cash_key] = logger

    return logger


def setup_default_loggers() -> Dict[str, logging.Logger]:
    """
    Настроqйки логгеров по умолчанию
    :return: словарь логеров

    ПРИМЕР:
    app_logger = get_or_create_loger(name="app") - логер приложения
    api_logger = get_or_create_loger(name="api") - логер для апи
    """
    logger = get_or_create_loger(name="log")

    return {
        'log': logger,
    }


logers_data = setup_default_loggers()

logger = logers_data["log"]

__all__ = ["logger"]
__version__ = "1.0.0"
__author__ = "Хабалашвили Павел"
