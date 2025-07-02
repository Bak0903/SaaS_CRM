# Contacts Service
Многоарендный backend-сервис для управления контактами.
Основан на Django + PostgreSQL + Celery + Redis. Поддерживает арендаторов через django-tenants.

## Требования
- Python 3.11+
- Poetry
- Docker + Docker Compose
- PostgreSQL 15+
- Redis 7+

## Быстрый старт (с Docker)
```
cp .env.example .env
docker compose up --build -d
```

## Создание схемы (тенанта) и миграций
```
docker compose exec web poetry run python manage.py create_schema acme AcmeCorp
```

## Примеры curl-запросов

### Создание контакта
```
curl -X POST http://127.0.0.1:8000/api/contacts/  \
 -H "Content-Type: application/json"   -H "X-SCHEMA: acme"   \
 -d '{"name": "John Doe", "email": "john@example.com", "phone": "+123456789"}'
```

### Получение всех контактов
```
curl -X GET http://localhost:8000/api/contacts/ \
-H "X-SCHEMA: acme"
```

### Редактирование контакта
```
curl -X PUT http://localhost:8000/api/contacts/<uuid> \
-H "X-SCHEMA: acme" \
-d '{"name": "bob", "email": "bob@example.com", "phone": "+123456789"}'
```
### Удаление контакта
```
curl -X DELETE http://localhost:8000/api/contacts/<uuid> \
-H "X-SCHEMA: acme"
```

## Тесты
```
docker compose exec web poetry run pytest
```

## Проверка стиля и безопасности
```
# Проверка кода на стиль
docker compose exec web poetry run flake8

# Проверка безопасности (bandit)
docker compose exec web poetry run bandit -r app
```

## Celery: Поиск "старых" контактов
```
docker compose exec web poetry run celery -A app worker --loglevel=info
```

## Время, потраченное на задание
~ 12 часов
