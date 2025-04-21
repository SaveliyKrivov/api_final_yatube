# 📘 Yatube API

**Yatube API** — это RESTful API для социальной сети, позволяющее пользователям публиковать записи, комментировать их, подписываться на авторов и управлять подписками.

---

## 🚀 Возможности

- 🔐 Аутентификация через JWT-токены
- 📝 CRUD-операции для постов и комментариев
- 👥 Управление подписками на авторов
- 📚 Группировка постов по категориям
- 🔍 Фильтрация и пагинация данных
- 🧪 Покрытие тестами с использованием `pytest`

---

## 🛠️ Технологии

- Python 3.7+
- Django 2.2
- Django REST Framework
- Simple JWT
- SQLite (по умолчанию)

---

## 📦 Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/SaveliyKrivov/api_final_yatube.git
   cd api_final_yatube
   ```

2. **Создайте и активируйте виртуальное окружение:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   # или
   venv\Scripts\activate  # Для Windows
   ```

3. **Установите зависимости:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Примените миграции:**

   ```bash
   python manage.py migrate
   ```

5. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver
   ```

---

## 🔑 Аутентификация

Для получения JWT-токена отправьте POST-запрос на эндпоинт:

```
/api/v1/jwt/create/
```

с телом запроса:

```json
{
  "username": "ваш_логин",
  "password": "ваш_пароль"
}
```

Полученный токен используйте в заголовке `Authorization` для доступа к защищённым ресурсам:

```
Authorization: Bearer ваш_токен
```

---

## 📚 Документация API

После запуска проекта, подробная документация доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

---

## 🧪 Тестирование

Для запуска тестов выполните:

```bash
pytest
```

---

## 👤 Автор

- [Савелий Кривов](https://github.com/SaveliyKrivov)
