# Flask Starter - Quick Reference

## Essential Commands

### Setup
```bash
./.claude/setup.sh           # Complete initial setup
make setup                   # Alternative with Makefile
```

### Development
```bash
make dev                     # Start both servers
make dev-backend            # Flask only
make dev-frontend           # Vite only
```

### Testing
```bash
make test                    # Run all tests
make test-cov               # With coverage report
pytest tests/test_auth.py   # Specific test file
```

### Database
```bash
make db-init                # Initialize database
make db-seed                # Seed sample data
make db-reset               # Reset database (CAUTION!)
flask db migrate            # Create migration
flask db upgrade            # Apply migrations
```

### Production
```bash
make build                  # Build for production
make run                    # Run with Gunicorn
gunicorn -c gunicorn_config.py app:app
```

### Code Quality
```bash
make format                 # Format with black
make lint                   # Check with flake8
```

### Docker
```bash
make docker-up              # Start containers
make docker-down            # Stop containers
make docker-logs            # View logs
```

## URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:5000 |
| API Docs | http://localhost:5000/api/v1/docs |
| Health Check | http://localhost:5000/health |

## Project Structure

```
app/
├── blueprints/    # Routes (main, api, auth)
├── models/        # Database models
├── utils/         # Helpers, validators, decorators
└── commands.py    # CLI commands

tests/             # Pytest test suite
docs/              # Documentation
.claude/           # Automation scripts
```

## API Endpoints

### Auth
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/refresh` - Refresh token

### Users
- `GET /api/v1/users` - List users
- `GET /api/v1/users/:id` - Get user
- `PUT /api/v1/users/:id` - Update user
- `DELETE /api/v1/users/:id` - Delete user

### Posts
- `GET /api/v1/posts` - List posts
- `GET /api/v1/posts/:id` - Get post
- `POST /api/v1/posts` - Create post
- `PUT /api/v1/posts/:id` - Update post
- `DELETE /api/v1/posts/:id` - Delete post

## Default Credentials

After seeding:
- Username: `admin`
- Password: `Admin123!`
- Email: `admin@example.com`

## Environment Variables

```bash
FLASK_ENV=development
FLASK_DEBUG=1
DATABASE_URL=sqlite:///app.db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
CORS_ORIGINS=http://localhost:5173
```

## Git Workflow

```bash
git checkout -b feature/your-feature
git add .
git commit -m "feat: Add your feature"
git push origin feature/your-feature
```

## Troubleshooting

### Port already in use
```bash
lsof -i :5000
kill -9 <PID>
```

### Database locked
```bash
rm app.db
flask init-db
flask seed-db
```

### Import errors
```bash
pip install -r requirements.txt --force-reinstall
```

## Documentation

- [README.md](../README.md) - Main documentation
- [API.md](API.md) - Complete API reference
- [WORKFLOW.md](WORKFLOW.md) - Development workflow
- [STRUCTURE.md](STRUCTURE.md) - Architecture overview

## Support

- GitHub: https://github.com/mk-knight23/48-starter-flask
- Issues: https://github.com/mk-knight23/48-starter-flask/issues
