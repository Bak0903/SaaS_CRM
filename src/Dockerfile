FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY pyproject.toml poetry.lock* /app/

RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install

COPY . /src/

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
