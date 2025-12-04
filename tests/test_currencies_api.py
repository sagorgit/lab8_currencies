"""Тесты для функции get_currencies.

Здесь проверяется, что функция возвращает
непустой список объектов Currency с корректными значениями.
"""

from __future__ import annotations

import unittest

from myapp.utils.currencies_api import get_currencies
from myapp.models import Currency


class GetCurrenciesTests(unittest.TestCase):
    """Набор тестов для функции get_currencies."""

    def test_returns_non_empty_list(self) -> None:
        """Функция должна возвращать непустой список."""
        currencies = get_currencies()
        self.assertIsInstance(currencies, list)
        self.assertGreater(len(currencies), 0)

    def test_all_items_are_currency_instances(self) -> None:
        """Каждый элемент списка должен быть экземпляром Currency."""
        currencies = get_currencies()
        for item in currencies:
            self.assertIsInstance(item, Currency)

    def test_currency_fields_are_valid(self) -> None:
        """Поля валют должны иметь разумные значения (номинал > 0, курс > 0)."""
        currencies = get_currencies()
        for c in currencies:
            self.assertGreater(c.nominal, 0)
            self.assertGreater(c.value, 0.0)
            self.assertIsInstance(c.char_code, str)
            self.assertTrue(c.char_code.strip())


if __name__ == "__main__":
    unittest.main()