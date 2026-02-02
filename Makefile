.PHONY: help install dev test build clean run db-init db-seed db-reset

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install all dependencies
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	npm install

dev:  ## Start development servers (backend + frontend)
	. venv/bin/activate && flask run &
	npm run dev

dev-backend:  ## Start Flask backend only
	. venv/bin/activate && flask run

dev-frontend:  ## Start Vite frontend only
	npm run dev

test:  ## Run all tests
	. venv/bin/activate && pytest

test-cov:  ## Run tests with coverage
	. venv/bin/activate && pytest --cov=app --cov-report=html

lint:  ## Run linting
	. venv/bin/activate && flake8 app/
	black --check app/

format:  ## Format code
	. venv/bin/activate && black app/

build:  ## Build for production
	npm run build
	. venv/bin/activate && pytest

run:  ## Run production server
	. venv/bin/activate && gunicorn -c gunicorn_config.py app:app

db-init:  ## Initialize database
	. venv/bin/activate && flask init-db

db-seed:  ## Seed database with sample data
	. venv/bin/activate && flask seed-db

db-reset:  ## Reset database
	. venv/bin/activate && flask reset-db

db-migrate:  ## Create new migration
	. venv/bin/activate && flask db migrate

db-upgrade:  ## Apply migrations
	. venv/bin/activate && flask db upgrade

clean:  ## Clean up generated files
	rm -rf build/
	rm -rf dist/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build:  ## Build Docker image
	docker-compose build

docker-up:  ## Start Docker containers
	docker-compose up -d

docker-down:  ## Stop Docker containers
	docker-compose down

docker-logs:  ## Show Docker logs
	docker-compose logs -f

setup:  ## Complete setup (install + init + seed)
	make install
	make db-init
	make db-seed
	@echo "✅ Setup complete! Run 'make dev' to start development servers"
