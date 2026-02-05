from ui_design.simple_cat_app import Ui_RandCatWindow

from api import get_random_cat
from .base_window import BaseWindow


class CatWindow(BaseWindow):
    """Окно с котами"""

    def setup_ui(self) -> None:
        """Настрока окна"""
        self.ui = Ui_RandCatWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(500, 600)
        self.setMaximumSize(500, 600)


    def setup_connections(self) -> None:
        """Настройка сигналов"""
        super().setup_connections()
        self.ui.pushButton.clicked.connect(self.show_cat_img)


    def show_cat_img(self) -> None:
        """Функция отображающее фото на странийце"""
        cat_url: str = get_random_cat()
        scaled_img = self._url_to_img(img_url=cat_url)

        self.ui.label.setPixmap(scaled_img)
