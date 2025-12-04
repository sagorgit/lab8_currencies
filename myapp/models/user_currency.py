"""Модуль связи пользователей и валют.

Здесь определён класс UserCurrency, который реализует
связь «многие ко многим» между пользователями и валютами.
"""

from __future__ import annotations


class UserCurrency:
    """Класс UserCurrency — связь пользователя и валюты.

    Атрибуты:
        id: Уникальный идентификатор записи связи.
        user_id: Внешний ключ на пользователя (ID из User).
        currency_id: Внешний ключ на валюту (ID из Currency).
    """

    def __init__(self, relation_id: int, user_id: int, currency_id: int) -> None:
        """Инициализирует связь между пользователем и валютой.

        Аргументы:
            relation_id: Идентификатор записи связи.
            user_id: Идентификатор пользователя.
            currency_id: Идентификатор валюты.

        Исключения:
            TypeError: если значения не являются целыми числами.
            ValueError: если какие-либо ID меньше или равны нулю.
        """
        self.id = relation_id
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> int:
        """Возвращает идентификатор записи связи."""
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """Устанавливает идентификатор связи с проверкой."""
        if not isinstance(value, int):
            raise TypeError("ID связи должен быть целым числом.")
        if value <= 0:
            raise ValueError("ID связи должен быть больше нуля.")
        self._id = value

    @property
    def user_id(self) -> int:
        """Возвращает идентификатор пользователя."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        """Устанавливает идентификатор пользователя с проверкой."""
        if not isinstance(value, int):
            raise TypeError("user_id должен быть целым числом.")
        if value <= 0:
            raise ValueError("user_id должен быть больше нуля.")
        self._user_id = value

    @property
    def currency_id(self) -> int:
        """Возвращает идентификатор валюты."""
        return self._currency_id

    @currency_id.setter
    def currency_id(self, value: int) -> None:
        """Устанавливает идентификатор валюты с проверкой."""
        if not isinstance(value, int):
            raise TypeError("currency_id должен быть целым числом.")
        if value <= 0:
            raise ValueError("currency_id должен быть больше нуля.")
        self._currency_id = value