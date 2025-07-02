FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . /app/

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
