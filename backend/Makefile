# Makefile для управления FastAPI-проектом

.PHONY: help install format lint type-check test run dev init-db shell

help:
	@echo "Доступные команды:"
	@echo "  make install     - Установить зависимости через poetry"
	@echo "  make format      - Форматировать код (black)"
	@echo "  make lint        - Проверить стиль кода (ruff)"
	@echo "  make type-check  - Проверить типы (mypy)"
	@echo "  make test        - Запустить тесты (pytest)"
	@echo "  make run         - Запустить сервер (uvicorn)"
	@echo "  make dev         - Запустить сервер в dev-режиме (uvicorn --reload)"
	@echo "  make init-db     - Инициализировать базы данных"
	@echo "  make shell       - Открыть shell"

install:
	poetry install

format:
	poetry run black .

lint:
	poetry run ruff check .

type-check:
	poetry run mypy .

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=app --cov-report=xml --cov-report=term-missing

run:
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000

dev:
	poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000

init-db:
	poetry run init-db 

shell:
	poetry shell