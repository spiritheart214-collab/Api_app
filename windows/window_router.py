from enum import Enum
from typing import Optional

from PyQt6.QtCore import QObject, pyqtSignal


class WindowType(Enum):
    """Типы окон в приложении"""
    CAT = 'cat'
    DOG = 'dog'
    RAND_MOVIE = 'rand_movie'
    MOVIE_BY_NAME = "movie_by_name"


class WindowRouter(QObject):
    """Централизованный роутер для навигации между окнами"""

    # Единый сигнал для переключения окон
    navigate = pyqtSignal(WindowType)

    def __init__(self):
        super().__init__()
        self.current_window: Optional[WindowType] = None

    def navigate_to_rand_cat(self) -> None:
        """Перейти к окну с котами"""
        self.navigate.emit(WindowType.CAT)
        self.current_window = WindowType.CAT

    def navigate_to_rand_dog(self) -> None:
        """Перейти к окну с Собаками"""
        self.navigate.emit(WindowType.DOG)
        self.current_window = WindowType.DOG

    def navigate_to_rand_movie(self) -> None:
        """Перейти к окну с фильмами"""
        self.navigate.emit(WindowType.RAND_MOVIE)
        self.current_window = WindowType.RAND_MOVIE

    def navigate_to_movie_by_name(self) -> None:
        """Перейти к окну поиска фильма по названию"""
        self.navigate.emit(WindowType.MOVIE_BY_NAME)
        self.current_window = WindowType.MOVIE_BY_NAME
