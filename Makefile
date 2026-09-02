.PHONY: help install install-dev run run-dev test test-cov lint format type-check clean docker-up docker-down migrate migrate-up migrate-down

help:
	@echo "SIGMUN - Sistema Integrado de Gestão Municipal"
	@echo ""
	@echo "Available commands:"
	@echo "  install       - Install production dependencies"
	@echo "  install-dev   - Install development dependencies"
	@echo "  run           - Run the application"
	@echo "  run-dev       - Run the application in development mode"
	@echo "  test          - Run tests"
	@echo "  test-cov      - Run tests with coverage"
	@echo "  lint          - Run linter"
	@echo "  format        - Format code"
	@echo "  type-check    - Run type checker"
	@echo "  clean         - Clean cache and temporary files"
	@echo "  docker-up     - Start Docker containers"
	@echo "  docker-down   - Stop Docker containers"
	@echo "  migrate       - Run database migrations"
	@echo "  migrate-up    - Apply database migrations"
	@echo "  migrate-down  - Rollback database migrations"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

run:
	uvicorn src.main:app --host 0.0.0.0 --port 8000

run-dev:
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term

test-integration:
	pytest tests/integration -v

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/
	isort src/ tests/

type-check:
	mypy src/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

docker-up:
	docker-compose -f docker-compose.yml up -d

docker-down:
	docker-compose -f docker-compose.yml down

migrate:
	alembic upgrade head

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1
