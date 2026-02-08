# Flask Production Deployment Guide

This guide provides comprehensive instructions for deploying the Flask application in production.

## 🚀 Quick Start

### Using Docker Compose (Recommended)

1. **Environment Variables**
```bash
# Copy and configure .env
cp .env.example .env
```

2. **Start Services**
```bash
docker-compose up -d
```

3. **Check Health**
```bash
curl https://localhost/health
```

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- PostgreSQL (or SQLite for development)
- Redis (for rate limiting)
- Nginx (for production)

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```env
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-here
API_VERSION=v1

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/flask_starter

# Redis Configuration
REDIS_URL=redis://localhost:6379/0

# Server Configuration
HOST=0.0.0.0
PORT=8000
WEB_CONCURRENCY=4

# SSL Configuration (for HTTPS)
SSL_CERTFILE=/path/to/cert.pem
SSL_KEYFILE=/path/to/key.pem
```

### Production vs Development

- **Production**:
  - `FLASK_ENV=production`
  - Stricter rate limiting
  - Security headers enabled
  - SSL required
- **Development**:
  - `FLASK_ENV=development`
  - Debug mode enabled
  - CORS configured for localhost

## 📦 Deployment Methods

### 1. Docker Compose (Recommended)

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://flask:flask@db:5432/flask_starter
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=flask_starter
      - POSTGRES_USER=flask
      - POSTGRES_PASSWORD=flask

  redis:
    image: redis:7-alpine

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
```

### 2. Manual Deployment

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
export FLASK_ENV=production
export DATABASE_URL=postgresql://user:pass@localhost/db
export REDIS_URL=redis://localhost:6379/0

# 3. Run migrations
flask db upgrade

# 4. Start with Gunicorn
gunicorn -c gunicorn_config.py app:app
```

### 3. Cloud Deployment

#### AWS EC2
1. Launch EC2 instance
2. Install Docker
3. Deploy with Docker Compose
4. Configure security groups (80, 443, 22)

#### Heroku
```bash
# Create Heroku app
heroku create your-app-name

# Set config vars
heroku config:set FLASK_ENV=production
heroku config:set DATABASE_URL=postgres://...

# Deploy
git push heroku main
```

## 🔒 Security Configuration

### SSL/TLS
1. Obtain SSL certificates (Let's Encrypt)
2. Configure Nginx for HTTPS
3. Set security headers

### Rate Limiting
- API: 10 requests/second
- Login: 5 requests/minute
- Overall: 200 requests/day

### Security Headers
- Strict-Transport-Security
- X-Frame-Options
- X-Content-Type-Options
- X-XSS-Protection
- Content-Security-Policy

## 📊 Monitoring

### Health Checks
- Application: `/health`
- Database: Connection check
- Redis: Connection check

### Logging
- Application logs: `logs/app.log`
- Access logs: Nginx logs
- Error logs: Nginx logs

### Monitoring with Prometheus
```yaml
# Add to docker-compose.yml
monitoring:
  image: prom/prometheus:latest
  ports:
    - "9090:9090"
  volumes:
    - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
```

## 🚦 Maintenance

### Database Migrations
```bash
# Create migration
flask db migrate -m "Migration message"

# Apply migration
flask db upgrade

# Rollback (if needed)
flask db downgrade
```

### Logs Rotation
- Application logs are automatically rotated (10MB, 5 backups)
- Configure Nginx log rotation separately

### Backups
```bash
# Database backup
pg_dump $DATABASE_URL > backup.sql

# Application backup
tar -czf backup.tar.gz app/ requirements.txt/
```

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection**
   - Check `DATABASE_URL` configuration
   - Verify database is running
   - Check network connectivity

2. **SSL Issues**
   - Verify SSL certificates
   - Check Nginx configuration
   - Test with SSL Labs

3. **Performance Issues**
   - Monitor CPU/Memory usage
   - Check database queries
   - Review rate limiting settings

4. **Memory Leaks**
   - Restart workers periodically
   - Monitor memory usage
   - Check for unclosed database connections

### Debug Mode
```bash
# Enable debug mode
export FLASK_ENV=development

# Run debug server
python app.py
```

## 📈 Scaling

### Horizontal Scaling
1. Load balancer (Nginx)
2. Multiple application instances
3. Shared database and Redis

### Vertical Scaling
1. Increase server resources
2. Optimize database queries
3. Use caching (Redis)

### Database Optimization
- Add indexes to frequently queried columns
- Use connection pooling
- Optimize query performance

## 🔧 Environment-Specific Configurations

### Development
```bash
export FLASK_ENV=development
export DEBUG=True
export DATABASE_URL=sqlite:///app.db
```

### Staging
```bash
export FLASK_ENV=production
export DEBUG=False
export DATABASE_URL=postgresql://user:pass@staging-db/db
```

### Production
```bash
export FLASK_ENV=production
export DEBUG=False
export DATABASE_URL=postgresql://user:pass@prod-db/db
export REDIS_URL=redis://prod-redis:6379/0
```

## 📝 Best Practices

1. **Environment Variables**
   - Never commit secrets to version control
   - Use environment-specific configurations
   - Document required variables

2. **Security**
   - Use HTTPS in production
   - Implement proper authentication
   - Validate all user inputs
   - Use parameterized queries

3. **Performance**
   - Use caching strategically
   - Optimize database queries
   - Implement proper indexing
   - Monitor performance metrics

4. **Monitoring**
   - Set up alerting
   - Monitor logs
   - Track key metrics
   - Regular health checks

## 🆘 Support

For issues and questions:
1. Check the logs in `logs/` directory
2. Review this deployment guide
3. Open an issue on GitHub
4. Contact the development team