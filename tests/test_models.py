"""Тесты для моделей предметной области.

Здесь проверяются классы:
Author, App, User, Currency, UserCurrency.
"""

from __future__ import annotations

import unittest

from myapp.models import Author, App, User, Currency, UserCurrency


class AuthorModelTests(unittest.TestCase):
    """Набор тестов для модели Author."""

    def test_author_creation_ok(self) -> None:
        """Проверяем, что автор создаётся с корректными данными."""
        author = Author(name="Тест Автор", group="P3123")
        self.assertEqual(author.name, "Тест Автор")
        self.assertEqual(author.group, "P3123")

    def test_author_empty_name_raises(self) -> None:
        """Проверяем, что пустое имя вызывает ValueError."""
        with self.assertRaises(ValueError):
            Author(name="", group="P3123")

    def test_author_wrong_type_raises(self) -> None:
        """Проверяем, что неверный тип для имени вызывает TypeError."""
        with self.assertRaises(TypeError):
            Author(name=123, group="P3123")  # type: ignore[arg-type]


class AppModelTests(unittest.TestCase):
    """Набор тестов для модели App."""

    def test_app_creation_ok(self) -> None:
        """Проверяем успешное создание App."""
        author = Author("Имя", "P3123")
        app = App(name="TestApp", version="1.0.0", author=author)
        self.assertEqual(app.name, "TestApp")
        self.assertEqual(app.version, "1.0.0")
        self.assertIs(app.author, author)

    def test_app_empty_name_raises(self) -> None:
        """Проверяем, что пустое название вызывает ValueError."""
        author = Author("Имя", "P3123")
        with self.assertRaises(ValueError):
            App(name="", version="1.0.0", author=author)

    def test_app_wrong_author_type_raises(self) -> None:
        """Проверяем, что неверный тип автора вызывает TypeError."""
        with self.assertRaises(TypeError):
            App(name="TestApp", version="1.0.0", author="строка")  # type: ignore[arg-type]


class UserModelTests(unittest.TestCase):
    """Набор тестов для модели User."""

    def test_user_creation_ok(self) -> None:
        """Проверяем корректное создание пользователя."""
        user = User(1, "Ali")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Ali")

    def test_user_negative_id_raises(self) -> None:
        """ID <= 0 должен вызывать ValueError."""
        with self.assertRaises(ValueError):
            User(0, "Ali")

    def test_user_wrong_name_type_raises(self) -> None:
        """Неверный тип имени вызывает TypeError."""
        with self.assertRaises(TypeError):
            User(1, 123)  # type: ignore[arg-type]


class CurrencyModelTests(unittest.TestCase):
    """Набор тестов для модели Currency."""

    def test_currency_creation_ok(self) -> None:
        """Проверяем корректное создание валюты."""
        cur = Currency(
            currency_id=1,
            num_code=840,
            char_code="USD",
            name="Доллар США",
            value=90.5,
            nominal=1,
        )
        self.assertEqual(cur.id, 1)
        self.assertEqual(cur.num_code, 840)
        self.assertEqual(cur.char_code, "USD")
        self.assertEqual(cur.name, "Доллар США")
        self.assertEqual(cur.nominal, 1)
        self.assertAlmostEqual(cur.value, 90.5)

    def test_currency_negative_value_raises(self) -> None:
        """Отрицательный курс должен вызывать ValueError."""
        with self.assertRaises(ValueError):
            Currency(
                currency_id=1,
                num_code=840,
                char_code="USD",
                name="Доллар США",
                value=-1.0,
                nominal=1,
            )

    def test_currency_zero_nominal_raises(self) -> None:
        """Номинал <= 0 должен вызывать ValueError."""
        with self.assertRaises(ValueError):
            Currency(
                currency_id=1,
                num_code=840,
                char_code="USD",
                name="Доллар США",
                value=90.5,
                nominal=0,
            )


class UserCurrencyModelTests(unittest.TestCase):
    """Набор тестов для модели UserCurrency."""

    def test_user_currency_creation_ok(self) -> None:
        """Проверяем создание связи пользователь-валюта."""
        link = UserCurrency(relation_id=1, user_id=2, currency_id=3)
        self.assertEqual(link.id, 1)
        self.assertEqual(link.user_id, 2)
        self.assertEqual(link.currency_id, 3)

    def test_user_currency_wrong_id_raises(self) -> None:
        """ID связи <= 0 должен вызывать ValueError."""
        with self.assertRaises(ValueError):
            UserCurrency(relation_id=0, user_id=2, currency_id=3)


if __name__ == "__main__":
    unittest.main()