from ui_design.simple_dog_app import Ui_RandDogWindow
from .base_window import BaseWindow

from api import get_random_dog
from log import function_logs


class DogWindow(BaseWindow):
    """Класс описыающий окно собаки"""

    def setup_ui(self):
        """Настрока окна"""
        self.ui = Ui_RandDogWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(500, 600)
        self.setMaximumSize(500, 600)

    def setup_connections(self):
        """Настройка сигналов"""
        super().setup_connections()
        self.ui.rand_dog_button.clicked.connect(self.show_dog)

    def show_dog(self):
        """Функция отображающее фото на странийце"""
        dog_url = get_random_dog()
        scaled_img = self._url_to_img(img_url=dog_url)
        self.ui.label.setPixmap(scaled_img)
        