# Contacts Service
Многоарендный backend-сервис для управления контактами.
Основан на Django + PostgreSQL + Celery + Redis. Поддерживает арендаторов через django-tenants.

# Требования
- Python 3.11+
- Poetry
- Docker + Docker Compose
- PostgreSQL 15+
- Redis 7+

# Быстрый старт (с Docker)
```
cp .env.example .env
docker compose up --build
```

# Создание схемы (тенанта) и миграций
```
docker compose exec web poetry run python manage.py create_tenant acme AcmeCorp
```

# Примеры curl-запросов

### Создание контакта
```
curl -X POST http://localhost:8000/api/contacts/ \
-H "X-SCHEMA: acme" \
-H "Content-Type: application/json" \
-d '{"full_name": "Rick Deckard", "email": "rick@blade.run", "phone": "+1234567"}'
```

### Получение всех контактов
```
curl -X GET http://localhost:8000/api/contacts/ \
-H "X-SCHEMA: acme"`
```

# Время, потраченное на задание
~ 12 часов
