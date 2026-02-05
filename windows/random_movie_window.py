from ui_design.rand_movie_window import Ui_RandMovieWindow
from .base_window import BaseWindow


class RandomFilmWindow(BaseWindow):
    """Окно с рандомными фильмами"""

    def setup_ui(self) -> None:
        """Настрока окна"""
        self.ui = Ui_RandMovieWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(680, 740)
        self.setMaximumSize(680, 740)

    def setup_connections(self) -> None:
        """Настройка сигналов"""
        super().setup_connections()
        self.ui.rand_movie_button.clicked.connect(self.show_random_movie)

    def show_random_movie(self) -> None:
        """Функция для отображения рандомного фильма"""
        film_data = self.kinopoisk.get_random_film()
        self._update_film_info(film_data=film_data)
