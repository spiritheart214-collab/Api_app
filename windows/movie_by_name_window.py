from ui_design.film_by_name_window import Ui_FilmByNameWindow
from .base_window import BaseWindow


class MovieByNameWindow(BaseWindow):
    """Окно поиска фильма по названию"""

    def setup_ui(self):
        """Настрока окна"""
        self.ui = Ui_FilmByNameWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(470, 852)
        self.setMaximumSize(470, 852)

    def setup_connections(self):
        """Настройка сигналов"""
        super().setup_connections()

        self.ui.find_movie_button.clicked.connect(self.find_film)

    def find_film(self) -> None:
        """Поиск фильма по названию"""
        film_name = self.ui.input_film.text().strip()
        film_data = self.kinopoisk.get_film_by_name(name=film_name)

        if "message" in film_data: # фильм не найден
            self.ui.label_poster.setText(film_data["message"])
        else:
            self._update_film_info(film_data=film_data)
