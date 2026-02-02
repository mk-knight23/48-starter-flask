# Flask Starter - Project Structure

Complete overview of the Flask Starter application architecture.

```
48-starter-flask/
├── app/                          # Main application package
│   ├── __init__.py
│   ├── app.py                    # Application factory
│   ├── commands.py               # Flask CLI commands
│   │
│   ├── blueprints/               # Route blueprints
│   │   ├── __init__.py
│   │   ├── main.py              # Main routes (serve frontend)
│   │   ├── api.py               # REST API endpoints (with Swagger)
│   │   └── auth.py              # Authentication endpoints
│   │
│   ├── models/                   # Database models
│   │   ├── __init__.py
│   │   ├── base.py              # Base model with mixins
│   │   └── user.py              # User and Post models
│   │
│   └── utils/                    # Utility functions
│       ├── __init__.py
│       ├── decorators.py        # Custom decorators (@admin_required)
│       ├── helpers.py           # Response helpers
│       └── validators.py        # Input validators
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── test_auth.py             # Authentication tests
│   └── test_api.py              # API endpoint tests
│
├── docs/                         # Documentation
│   ├── API.md                   # Complete API reference
│   ├── WORKFLOW.md              # Development workflow
│   ├── ARCHITECTURE.md          # Architecture overview
│   ├── DESIGN.md                # Design system
│   └── STRUCTURE.md             # This file
│
├── .claude/                      # Claude AI workflows
│   └── scripts/
│       ├── setup.sh             # Initial setup
│       ├── dev.sh               # Start dev servers
│       ├── test.sh              # Run tests
│       └── build.sh             # Production build
│
├── src/                          # React frontend
│   ├── App.tsx
│   ├── main.tsx
│   └── ...
│
├── .env.example                  # Environment template
├── .gitignore
├── .flake8                       # Linting config
├── pytest.ini                    # Test config
├── requirements.txt              # Python dependencies
├── package.json                  # Node dependencies
├── Makefile                      # Common commands
├── Dockerfile                    # Container image
├── docker-compose.yml            # Development containers
├── gunicorn_config.py           # Production server config
└── README.md                     # Main documentation
```

## Architecture Layers

### 1. Application Layer
- **app.py**: Application factory with configuration
- **blueprints/**: Modular route organization
  - `main.py`: Frontend serving and basic routes
  - `api.py`: RESTful API with Swagger docs
  - `auth.py`: JWT authentication

### 2. Data Layer
- **models/**: SQLAlchemy ORM models
  - `base.py`: Common base classes
  - `user.py`: User and Post models
  - TimestampMixin: Auto-updating timestamps

### 3. Business Logic Layer
- **utils/**: Reusable utilities
  - `validators.py`: Input validation
  - `decorators.py`: Access control
  - `helpers.py`: Response formatting

### 4. Testing Layer
- **tests/**: Pytest test suite
  - Unit tests for all endpoints
  - Fixtures for common scenarios
  - Coverage reporting

## Key Design Patterns

### Factory Pattern
```python
def create_app(config_name='development'):
    app = Flask(__name__)
    # Initialize extensions
    # Register blueprints
    return app
```

### Blueprint Pattern
- Separates concerns (auth, api, main)
- Easy to add new features
- Clean URL structure

### Repository Pattern
```python
class BaseModel:
    def save(self): ...
    def delete(self): ...
    def to_dict(self): ...
```

## API Endpoint Structure

```
/api/v1/
├── docs           # Swagger UI
├── auth/
│   ├── register
│   ├── login
│   ├── me
│   └── refresh
├── users/
│   ├── GET    /       # List users
│   ├── POST   /       # Create user
│   ├── GET    /:id    # Get user
│   ├── PUT    /:id    # Update user
│   └── DELETE /:id    # Delete user
└── posts/
    ├── GET    /       # List posts
    ├── POST   /       # Create post
    ├── GET    /:id    # Get post
    ├── PUT    /:id    # Update post
    └── DELETE /:id    # Delete post
```

## Database Schema

### users
- id (PK)
- username (unique)
- email (unique)
- password_hash
- first_name
- last_name
- is_admin
- last_login
- created_at
- updated_at

### posts
- id (PK)
- title
- content
- summary
- published
- user_id (FK)
- created_at
- updated_at

## Environment Configuration

Development (.env):
```
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=sqlite:///app.db
```

Production:
```
FLASK_ENV=production
DATABASE_URL=postgresql://...
SECRET_KEY=<strong-secret>
```

## Extension Integrations

1. **Flask-SQLAlchemy**: ORM and database
2. **Flask-Migrate**: Database migrations
3. **Flask-JWT-Extended**: JWT authentication
4. **Flask-CORS**: Cross-origin requests
5. **Flask-RESTX**: API documentation
6. **Flask-Bcrypt**: Password hashing

## Security Features

- Password hashing with bcrypt
- JWT token authentication
- CORS configuration
- Input validation
- SQL injection prevention (ORM)
- XSS protection
- Rate limiting ready

## Development Workflow

1. **Setup**: `.claude/setup.sh`
2. **Develop**: `make dev`
3. **Test**: `make test`
4. **Format**: `make format`
5. **Lint**: `make lint`
6. **Build**: `make build`
7. **Deploy**: `make run`

## Production Ready

- Gunicorn WSGI server
- Docker containerization
- Environment-based config
- Error handling
- Logging
- Health checks
- Database migrations
- Static file serving
