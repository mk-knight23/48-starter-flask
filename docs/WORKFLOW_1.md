# Development Workflow

Complete guide for developing with Flask Starter.

## Initial Setup

```bash
# Clone the repository
git clone https://github.com/mk-knight23/48-starter-flask.git
cd 48-starter-flask

# Run setup script
./claude/setup.sh
```

## Daily Development

### Start Development Servers

```bash
# Option 1: Use the dev script
./.claude/scripts/dev.sh

# Option 2: Use Make
make dev

# Option 3: Start manually
flask run
npm run dev
```

### Development URLs

- Frontend: http://localhost:5173
- Backend API: http://localhost:5000
- API Docs: http://localhost:5000/api/v1/docs

## Code Quality

```bash
# Format code
make format

# Run linter
make lint

# Run tests
make test
```

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/add-feature

# Commit changes
git add .
git commit -m "feat: Add new feature"

# Push and create PR
git push origin feature/add-feature
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest tests/test_auth.py
```

## Database Management

```bash
# Create migration
flask db migrate -m "Description"

# Apply migrations
flask db upgrade

# Reset database
flask reset-db

# Seed data
flask seed-db
```

## Deployment

```bash
# Build frontend
npm run build

# Start production server
gunicorn -c gunicorn_config.py app:app
```

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTX Docs](https://flask-restx.readthedocs.io/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
