"""Модуль модели приложения.

Здесь определён класс App, который хранит
информацию о названии приложения, версии
и объекте автора.
"""

from __future__ import annotations

from .author import Author


class App:
    """Класс App — представляет само приложение.

    Атрибуты:
        name: Название приложения.
        version: Версия приложения в виде строки (например, "1.0.0").
        author: Объект автора приложения (экземпляр класса Author).
    """

    def __init__(self, name: str, version: str, author: Author) -> None:
        """Инициализирует новый объект App.

        Аргументы:
            name: Название приложения.
            version: Версия приложения.
            author: Объект автора (класс Author).

        Исключения:
            TypeError: если типы аргументов неверные.
            ValueError: если name или version пустые строки.
        """
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self) -> str:
        """Возвращает название приложения."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает название приложения с проверкой.

        Исключения:
            TypeError: если значение не строка.
            ValueError: если строка пустая.
        """
        if not isinstance(value, str):
            raise TypeError("Название приложения должно быть строкой.")
        if not value.strip():
            raise ValueError("Название приложения не может быть пустым.")
        self._name = value

    @property
    def version(self) -> str:
        """Возвращает версию приложения."""
        return self._version

    @version.setter
    def version(self, value: str) -> None:
        """Устанавливает версию приложения с проверкой.

        Ожидается строка вида '1.0.0', но строгий формат
        здесь не проверяется, только непустая строка.
        """
        if not isinstance(value, str):
            raise TypeError("Версия приложения должна быть строкой.")
        if not value.strip():
            raise ValueError("Версия приложения не может быть пустой.")
        self._version = value

    @property
    def author(self) -> Author:
        """Возвращает объект автора приложения."""
        return self._author

    @author.setter
    def author(self, value: Author) -> None:
        """Устанавливает объект автора приложения.

        Исключения:
            TypeError: если значение не является экземпляром Author.
        """
        if not isinstance(value, Author):
            raise TypeError("author должен быть экземпляром класса Author.")
        self._author = value