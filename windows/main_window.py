from PyQt6.QtWidgets import QStackedWidget

from .cat_window import CatWindow
from .dog_window import DogWindow
from .movie_by_name_window import MovieByNameWindow
from .random_movie_window import RandomFilmWindow
from .window_router import WindowType, WindowRouter


class MainWindow(QStackedWidget):
    """Главное окно приложения с пререклбчением между ними"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("API APP")

        # Создаем роутер
        self.router = WindowRouter()
        self.router.navigate.connect(self.handle_navigation)

        # Создаем окна с передачей роутера
        self.rand_cat_window = CatWindow(router=self.router)
        self.rand_dog_window = DogWindow(router=self.router)
        self.rand_film_window = RandomFilmWindow(router=self.router)
        self.movie_by_name = MovieByNameWindow(router=self.router)

        # Добавляем окна в stacked widget
        self.addWidget(self.rand_cat_window)
        self.addWidget(self.rand_dog_window)
        self.addWidget(self.rand_film_window)
        self.addWidget(self.movie_by_name)

        self.router.navigate_to_rand_cat()

    def handle_navigation(self, window_type: WindowType):
        """Обработчик навигации от роутера"""
        if window_type == WindowType.CAT:
            self.setCurrentWidget(self.rand_cat_window)
            self.setWindowTitle("Рандомные коты")
            self.resize(self.rand_cat_window.size())
            self.setFixedSize(self.rand_cat_window.size())
        elif window_type == WindowType.RAND_MOVIE:
            self.setCurrentWidget(self.rand_film_window)
            self.setWindowTitle("Рандомные фильмы")
            self.resize(self.rand_film_window.size())
            self.setFixedSize(self.rand_film_window.size())
        elif window_type == WindowType.MOVIE_BY_NAME:
            self.setCurrentWidget(self.movie_by_name)
            self.setWindowTitle("Поиск фильма")
            self.resize(self.movie_by_name.size())
            self.setFixedSize(self.movie_by_name.size())
        elif window_type == WindowType.DOG:
            self.setCurrentWidget(self.rand_dog_window)
            self.setWindowTitle("Рандомные собаки")
            self.resize(self.rand_dog_window.size())
            self.setFixedSize(self.rand_dog_window.size())
