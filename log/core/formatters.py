"""
Форматирование для логера
"""
import logging
from typing import Dict

from .config import COLOR_SCHEMES, LOG_CONFIG


class ColorFormatter(logging.Formatter):
    """Класс настройщик цветного выода в консоль"""

    def __init__(self, fmt: str = None, datefmt: str = None, color_scheme: str = "default") -> None:
        """Инициализация базовых настроек"""

        self._first_initialized_passed = False
        self.fmt = fmt
        self.datefmt = datefmt
        self.colors = color_scheme

        super().__init__(fmt=self.fmt, datefmt=self.datefmt)

        self._first_initialized_passed = True# отслеживание инициализации

    @property
    def fmt(self) -> str:
        """Геттер: возращает шаблон отображения логов"""
        return self._fmt

    @fmt.setter
    def fmt(self, value: str) -> None:
        """Сеттер: валидирует установку шаблона отображения логов"""
        self._fmt = LOG_CONFIG["format"] if value is None else value

        # вызвть супер метод только если используется ссетер после перой инициализации
        if self._first_initialized_passed:
            super().__init__(fmt=self._fmt, datefmt=self._datefmt)

    @property
    def datefmt(self) -> str:
        """Геттер: возращает шаблон отображения дата/время у логов"""
        return self._datefmt

    @datefmt.setter
    def datefmt(self, value: str) -> None:
        """Сеттер: валидирует установку дата/время логов"""
        self._datefmt = LOG_CONFIG["date_format"] if value is None else value

        # вызвть супер метод только если используется ссетер после перой инициализации
        if self._first_initialized_passed:
            super().__init__(fmt=self._fmt, datefmt=self._datefmt)

    @property
    def colors(self) -> Dict[str, str]:
        """Геттер: возращает шаблон цветовой схемы"""

        return self._colors

    @colors.setter
    def colors(self, value: str) -> None:
        """Сеттер : изменить цветовую схему"""
        self._colors = COLOR_SCHEMES.get(value, COLOR_SCHEMES["default"])

    def format(self, record: logging.LogRecord) -> str:
        """Форматирует запись с добавлением цвета"""
        color = self.colors.get(record.levelname, self.colors['RESET'])
        message = super().format(record)
        return f"{color}{message}{self.colors['RESET']}"
