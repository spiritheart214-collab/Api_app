import sys

from PyQt6.QtWidgets import QApplication

from windows import MainWindow
from log import logger, function_logs


@function_logs
def main() -> None:
    """Основаная функция запуска приложения. Точка входа в программу"""
    app = QApplication(sys.argv)

    app.setStyle('Fusion')

    window = MainWindow()
    window.show()

    logger.info("Приложение запущено успешно")
    sys.exit(app.exec())

if __name__ == '__main__':
    """
    Точка входа при запуске скрипта напрямую.
    """
    logger.info("=" * 50)
    logger.info("Запуск приложения API APP")
    logger.info("=" * 50)

    main()
