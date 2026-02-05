"""
Конфигура для логера
"""
import logging
from typing import Any, Dict

# Основные кофигурации
LOG_CONFIG: Dict[str, Any] = {
    'default_level': logging.DEBUG,
    'date_format': "%d.%m.%Y %H:%M",
    'format': "%(asctime)s \t|\t [%(levelname)-8s] \t|\t %(message)s",
}

# Цветовые схемы
COLOR_SCHEMES: Dict[str, Dict[str, str]] = {
    'default': {
        'DEBUG': '\033[36m',  # голубой
        'INFO': '\033[32m',  # зеленый
        'WARNING': '\033[33m',  # желтый
        'ERROR': '\033[31m',  # красный
        'CRITICAL': '\033[1;31m',  # жирный красный
        'RESET': '\033[0m'
    },
    'bright': {
        'DEBUG': '\033[96m',  # яркий голубой
        'INFO': '\033[92m',  # яркий зеленый
        'WARNING': '\033[93m',  # яркий желтый
        'ERROR': '\033[91m',  # яркий красный
        'CRITICAL': '\033[1;97;41m',  # белый на красном фоне
        'RESET': '\033[0m'
    },
    'pastel': {
        'DEBUG': '\033[38;5;153m',  # пастельно-голубой
        'INFO': '\033[38;5;114m',  # пастельно-зеленый
        'WARNING': '\033[38;5;221m',  # пастельно-желтый
        'ERROR': '\033[38;5;210m',  # пастельно-красный
        'CRITICAL': '\033[48;5;210;38;5;0m',  # черный на пастельно-красном
        'RESET': '\033[0m'
    },
    'monochrome': {
        'DEBUG': '\033[90m',  # серый
        'INFO': '\033[97m',  # белый
        'WARNING': '\033[93m',  # желтый
        'ERROR': '\033[91m',  # красный
        'CRITICAL': '\033[1;91m',  # жирный красный
        'RESET': '\033[0m'
    }
}
