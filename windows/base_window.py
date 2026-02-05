import requests
from abc import ABC, abstractmethod
from typing import Dict, Union

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt

from api import Kinopoisk
from .window_router import WindowRouter


class _QMainWindowMeta(type(QMainWindow), type(ABC)):
    """Метакласс для объединения QMainWindow и ABC"""
    pass


class BaseWindow(QMainWindow, ABC, metaclass=_QMainWindowMeta):
    """Базовый абстрактный класс для всех окон"""

    def __init__(self, router: WindowRouter = None) -> None:
        """Автоматический вызов настройки интерфесов и сигналов"""
        super().__init__()
        self.kinopoisk = Kinopoisk()
        self.ui = None
        self.router = router
        self.setup_ui()
        self.setup_connections()

    @abstractmethod
    def setup_ui(self):
        """Настройка интерфейса"""
        pass

    @abstractmethod
    def setup_connections(self):
        """Настройка сигналов"""
        self.ui.action_random_cat.triggered.connect(self.router.navigate_to_rand_cat)
        self.ui.action_random_film.triggered.connect(self.router.navigate_to_rand_movie)
        self.ui.action_film_by_name.triggered.connect(self.router.navigate_to_movie_by_name)
        self.ui.action_random_dog.triggered.connect(self.router.navigate_to_rand_dog)

    @staticmethod
    def _url_to_img(img_url: str) -> QPixmap:
        """
        Функция для конвертации конвретации изображения из ссылки в изображение для просмотра
        :param img_url: ссылка на изображение в типе данных str
        :return: маштабированное изображение в типе данных QPixmap для последующего отображение в приложении
        """
        response = requests.get(url=img_url)


        pixmap = QPixmap()
        pixmap.loadFromData(response.content)

        scaled_img = pixmap.scaled(300, 300,
                                   Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)

        return scaled_img

    def _update_film_info(self, film_data: Dict[str, Union[str, int]]) -> None:
        """Функция принимает словарь данных о фильме и устанавливает их в окно"""
        name, description, year, poster = [str(film_value)
                                           if isinstance(film_value, int) else film_value
                                           for film_value in film_data.values()]

        short_descr = description[:150] + "..."
        scaled_img = self._url_to_img(img_url=poster)

        self.ui.label_name.setText(name)
        self.ui.label_year.setText(year)
        self.ui.label_description.setText(short_descr)
        self.ui.label_poster.setPixmap(scaled_img)

