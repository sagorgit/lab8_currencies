"""Главный модуль приложения.

Запускает HTTP-сервер, настраивает окружение Jinja2
и обрабатывает основные маршруты:
'/', '/users', '/user', '/currencies', '/author'.
"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from typing import List, Dict, Any, Optional

from jinja2 import Environment, PackageLoader, select_autoescape

from .models import Author, App, User
from .utils.currencies_api import get_currencies


# --- Глобальные объекты предметной области ---

# Укажи здесь свои реальные данные
main_author = Author(name="Сагор Афсар Уддин", group="P3123")

app_info = App(
    name="CurrenciesListApp",
    version="1.0.0",
    author=main_author,
)

# Простейший список пользователей (пока без базы данных)
USERS: List[User] = [
    User(1, "Ali"),
    User(2, "Ivan"),
    User(3, "Maria"),
]

# Подписки: user_id -> список символьных кодов валют
USER_SUBSCRIPTIONS: Dict[int, List[str]] = {
    1: ["USD", "EUR"],
    2: ["USD"],
    3: [],
}

# --- Настройка Jinja2 Environment ---

env = Environment(
    loader=PackageLoader("myapp"),  # шаблоны ищутся в myapp/templates
    autoescape=select_autoescape()
)

template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")
template_user_detail = env.get_template("user_detail.html")
template_author = env.get_template("author.html")


def build_navigation() -> List[Dict[str, Any]]:
    """Возвращает список пунктов навигации для меню."""
    return [
        {"caption": "Главная", "href": "/"},
        {"caption": "Пользователи", "href": "/users"},
        {"caption": "Валюты", "href": "/currencies"},
        {"caption": "Об авторе", "href": "/author"},
    ]


def find_user_by_id(user_id: int) -> Optional[User]:
    """Ищет пользователя в списке USERS по его ID."""
    for user in USERS:
        if user.id == user_id:
            return user
    return None


class MyRequestHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов для нашего приложения."""

    def _send_html(self, html: str, status_code: int = 200) -> None:
        """Отправляет HTML-ответ клиенту."""
        self.send_response(status_code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_GET(self) -> None:
        """Обрабатывает все входящие GET-запросы."""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)

        if path == "/":
            self.handle_index()
        elif path == "/users":
            self.handle_users()
        elif path == "/currencies":
            self.handle_currencies()
        elif path == "/author":
            self.handle_author()
        elif path == "/user":
            self.handle_user_detail(query)
        else:
            self.handle_not_found()

    def handle_index(self) -> None:
        """Обрабатывает маршрут '/' (главная страница)."""
        html_content = template_index.render(
            app_name=app_info.name,
            app_version=app_info.version,
            author_name=main_author.name,
            group=main_author.group,
            navigation=build_navigation(),
        )
        self._send_html(html_content)

    def handle_users(self) -> None:
        """Обрабатывает маршрут '/users' — список пользователей."""
        html_content = template_users.render(
            app_name=app_info.name,
            author_name=main_author.name,
            group=main_author.group,
            navigation=build_navigation(),
            users=USERS,
        )
        self._send_html(html_content)

    def handle_currencies(self) -> None:
        """Обрабатывает маршрут '/currencies' — список валют."""
        currencies = get_currencies()
        html_content = template_currencies.render(
            app_name=app_info.name,
            author_name=main_author.name,
            group=main_author.group,
            navigation=build_navigation(),
            currencies=currencies,
        )
        self._send_html(html_content)

    def handle_author(self) -> None:
        """Обрабатывает маршрут '/author' — информация об авторе."""
        html_content = template_author.render(
            app_name=app_info.name,
            author_name=main_author.name,
            group=main_author.group,
            navigation=build_navigation(),
        )
        self._send_html(html_content)

    def handle_user_detail(self, query: Dict[str, List[str]]) -> None:
        """Обрабатывает маршрут '/user?id=...' — страница пользователя."""
        # Проверяем, что параметр id передан
        if "id" not in query:
            self._send_html("<h1>Ошибка: параметр id не указан</h1>", status_code=400)
            return

        try:
            user_id = int(query["id"][0])
        except ValueError:
            self._send_html("<h1>Ошибка: id должен быть числом</h1>", status_code=400)
            return

        user = find_user_by_id(user_id)
        if user is None:
            self._send_html("<h1>Пользователь не найден</h1>", status_code=404)
            return

        # Получаем все валюты и фильтруем только те, на которые подписан пользователь
        all_currencies = get_currencies()
        subscribed_codes = USER_SUBSCRIPTIONS.get(user.id, [])
        subscriptions = [
            c for c in all_currencies if c.char_code in subscribed_codes
        ]

        html_content = template_user_detail.render(
            app_name=app_info.name,
            author_name=main_author.name,
            group=main_author.group,
            navigation=build_navigation(),
            user=user,
            subscriptions=subscriptions,
        )
        self._send_html(html_content)

    def handle_not_found(self) -> None:
        """Отправляет простую страницу 404, если маршрут не найден."""
        html_content = (
            "<html><head><meta charset='UTF-8'><title>404</title></head>"
            "<body><h1>404 — Страница не найдена</h1></body></html>"
        )
        self._send_html(html_content, status_code=404)


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Запускает HTTP-сервер на указанном хосте и порту."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Сервер запущен на http://{host}:{port}/ (нажмите Ctrl+C для остановки)")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()