"""
Модуль собирает пакет по работе/настройке логера из пакета 'core' и 'log_decorators'
"""
from .core import logger
from .log_decorators import class_logs, function_logs

__all__ = ["logger", "class_logs", "function_logs"]
__version__ = "1.0.0"
__author__ = "Хабалашвили Павел"
