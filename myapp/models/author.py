"""Модуль моделей, связанных с автором приложения.

Здесь определён класс Author, который хранит
информацию об имени автора и его учебной группе.
"""

from __future__ import annotations


class Author:
    """Класс Author — представляет автора приложения.

    Атрибуты:
        name: Полное имя автора.
        group: Учебная группа автора (например, "P3123").
    """

    def __init__(self, name: str, group: str) -> None:
        """Инициализация объекта Author.

        Аргументы:
            name: Имя автора.
            group: Учебная группа.

        Исключения:
            TypeError: если name или group не являются строками.
            ValueError: если передана пустая строка.
        """
        self.name = name
        self.group = group

    @property
    def name(self) -> str:
        """Возвращает полное имя автора."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает имя автора с проверкой корректности.

        Аргументы:
            value: Новое значение имени.

        Исключения:
            TypeError: если значение не строка.
            ValueError: если строка пустая.
        """
        if not isinstance(value, str):
            raise TypeError("Имя автора должно быть строкой.")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым.")
        self._name = value

    @property
    def group(self) -> str:
        """Возвращает учебную группу автора."""
        return self._group

    @group.setter
    def group(self, value: str) -> None:
        """Устанавливает группу автора с проверкой.

        Аргументы:
            value: Новое значение группы (например, 'P3123').

        Исключения:
            TypeError: если значение не строка.
            ValueError: если строка пустая.
        """
        if not isinstance(value, str):
            raise TypeError("Группа должна быть строкой.")
        if not value.strip():
            raise ValueError("Группа не может быть пустой.")
        self._group = value