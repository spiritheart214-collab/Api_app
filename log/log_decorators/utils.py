"""Модуль вспомогательных функций для визуализации логирования"""
from typing import Any, Dict


def _args_to_str(arguments: tuple) -> str:
    """
    Форматирует аргументы для логирования.
    Автоматически пропускает self для методов класса.
    """
    if not arguments:
        return ""

    # Если первый аргумент похож на self (экземпляр класса)
    # и это не единственный аргумент - пропускаем его
    if (len(arguments) > 0 and
            hasattr(arguments[0], '__class__') and
            not isinstance(arguments[0], type)):  # Проверяем что это не сам класс
        # Скорее всего это self, пропускаем
        args_to_format = arguments[1:]
    else:
        args_to_format = arguments

    if not args_to_format:
        return ""

    # Форматируем аргументы
    result = []
    for arg in args_to_format:
        if isinstance(arg, str):
            result.append(f"'{arg}'")
        else:
            result.append(str(arg))

    return ", ".join(result)


def _kwargs_to_str(keyword_args: Dict[str, Any]) -> str:
    """
     Функция для отображения подучених аргов от другой функции в теримнале при логировании.
    :param keyword_args: словарь кваргов
    :return: строковое представление кваргов
    """
    if keyword_args:
        kwargs_list = [f"{key}={value}" for key, value in keyword_args.items()]
        kwars_str = ", ".join(kwargs_list) if len(kwargs_list) > 1 else kwargs_list[0]
        return kwars_str
    return ""


def _kwargs_view(keyword_args: Dict[str, Any]) -> str:
    """Представления в читабельном виде болшьших словарей"""
    kwargs_str = "{\n"

    for key, value in keyword_args.items():
        kwargs_str += f"\t{key}: value\n"

    kwargs_str += "}"
    return kwargs_str

