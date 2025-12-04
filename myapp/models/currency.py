"""Модуль модели валюты.

Здесь определён класс Currency, который представляет
информацию об отдельной валюте и её курсе.
"""

from __future__ import annotations


class Currency:
    """Класс Currency — описывает валюту.

    Атрибуты:
        id: Уникальный целочисленный идентификатор валюты.
        num_code: Цифровой код валюты (например, 360).
        char_code: Буквенный код валюты (например, "IDR").
        name: Название валюты (например, "Рупий").
        value: Курс валюты в виде числа с плавающей точкой.
        nominal: Номинал, за какое количество единиц указан курс.
    """

    def __init__(
        self,
        currency_id: int,
        num_code: int,
        char_code: str,
        name: str,
        value: float,
        nominal: int,
    ) -> None:
        """Инициализирует объект Currency.

        Аргументы:
            currency_id: Идентификатор записи валюты.
            num_code: Цифровой код валюты.
            char_code: Символьный код (например, 'USD').
            name: Название валюты.
            value: Курс валюты.
            nominal: Номинал, для которого указан курс.

        Исключения:
            TypeError: если типы аргументов неверные.
            ValueError: если числовые значения неположительные
                или строки пустые.
        """
        self.id = currency_id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> int:
        """Возвращает идентификатор валюты."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Устанавливает идентификатор валюты с проверкой."""
        if not isinstance(value, int):
            raise TypeError("ID валюты должен быть целым числом.")
        if value <= 0:
            raise ValueError("ID валюты должен быть больше нуля.")
        self._id = value

    @property
    def num_code(self) -> int:
        """Возвращает цифровой код валюты."""
        return self._num_code

    @num_code.setter
    def num_code(self, value: int) -> None:
        """Устанавливает цифровой код валюты."""
        if not isinstance(value, int):
            raise TypeError("Цифровой код валюты должен быть целым числом.")
        if value <= 0:
            raise ValueError("Цифровой код валюты должен быть больше нуля.")
        self._num_code = value

    @property
    def char_code(self) -> str:
        """Возвращает символьный код валюты."""
        return self._char_code

    @char_code.setter
    def char_code(self, value: str) -> None:
        """Устанавливает символьный код валюты с проверкой."""
        if not isinstance(value, str):
            raise TypeError("Символьный код валюты должен быть строкой.")
        if not value.strip():
            raise ValueError("Символьный код валюты не может быть пустым.")
        self._char_code = value

    @property
    def name(self) -> str:
        """Возвращает название валюты."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает название валюты с проверкой."""
        if not isinstance(value, str):
            raise TypeError("Название валюты должно быть строкой.")
        if not value.strip():
            raise ValueError("Название валюты не может быть пустым.")
        self._name = value

    @property
    def value(self) -> float:
        """Возвращает текущий курс валюты."""
        return self._value

    @value.setter
    def value(self, amount: float) -> None:
        """Устанавливает курс валюты с проверкой.

        Курс должен быть положительным числом.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Курс валюты должен быть числом.")
        if amount <= 0:
            raise ValueError("Курс валюты должен быть больше нуля.")
        self._value = float(amount)

    @property
    def nominal(self) -> int:
        """Возвращает номинал валюты."""
        return self._nominal

    @nominal.setter
    def nominal(self, value: int) -> None:
        """Устанавливает номинал валюты с проверкой."""
        if not isinstance(value, int):
            raise TypeError("Номинал должен быть целым числом.")
        if value <= 0:
            raise ValueError("Номинал должен быть больше нуля.")
        self._nominal = value