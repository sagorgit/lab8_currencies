"""Модуль модели пользователя.

Здесь определён класс User, который описывает
пользователя системы по его идентификатору и имени.
"""

from __future__ import annotations


class User:
    """Класс User — представляет пользователя приложения.

    Атрибуты:
        id: Целочисленный уникальный идентификатор пользователя.
        name: Имя пользователя.
    """

    def __init__(self, user_id: int, name: str) -> None:
        """Инициализирует нового пользователя.

        Аргументы:
            user_id: Уникальный идентификатор пользователя.
            name: Имя пользователя.

        Исключения:
            TypeError: если типы аргументов неверные.
            ValueError: если id <= 0 или name пустая строка.
        """
        self.id = user_id
        self.name = name

    @property
    def id(self) -> int:
        """Возвращает идентификатор пользователя."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Устанавливает идентификатор пользователя с проверкой.

        Исключения:
            TypeError: если значение не целое число.
            ValueError: если значение меньше или равно нулю.
        """
        if not isinstance(value, int):
            raise TypeError("ID пользователя должен быть целым числом.")
        if value <= 0:
            raise ValueError("ID пользователя должен быть больше нуля.")
        self._id = value

    @property
    def name(self) -> str:
        """Возвращает имя пользователя."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает имя пользователя с проверкой.

        Исключения:
            TypeError: если значение не строка.
            ValueError: если строка пустая.
        """
        if not isinstance(value, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя пользователя не может быть пустым.")
        self._name = value