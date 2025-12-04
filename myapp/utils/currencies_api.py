"""Модуль для получения курсов валют.

В этой простой версии функция get_currencies возвращает
несколько тестовых валют. Позже сюда можно подключить
реальный запрос к API (например, ЦБ РФ).
"""

from __future__ import annotations
from typing import List
from ..models import Currency


def get_currencies() -> List[Currency]:
    """Возвращает список тестовых валют.

    Сейчас данные «зашиты» в коде, чтобы упростить
    разработку и демонстрацию работы шаблонов.
    """
    return [
        Currency(
            currency_id=1,
            num_code=840,
            char_code="USD",
            name="Доллар США",
            value=90.5,
            nominal=1,
        ),
        Currency(
            currency_id=2,
            num_code=978,
            char_code="EUR",
            name="Евро",
            value=95.2,
            nominal=1,
        ),
        Currency(
            currency_id=3,
            num_code=643,
            char_code="RUB",
            name="Российский рубль",
            value=1.0,
            nominal=1,
        ),
    ]