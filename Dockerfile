FROM python:3.11-slim

# Set metadata
LABEL maintainer="Flask Starter Team"
LABEL description="Flask Starter with React frontend - Production Ready"
LABEL version="1.0.0"

# Set working directory
WORKDIR /app

# Create logs directory
RUN mkdir -p /app/logs

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check with improved logging
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Create startup script
RUN echo '#!/bin/bash\n\
set -e\n\
# Wait for database if needed\n\
# python /app/wait-for-db.py\n\
# Run migrations\n\
python -c "from app import create_app; app = create_app(\"production\"); with app.app_context(): from flask_migrate import upgrade; upgrade()"\n\
# Start the application\n\
exec gunicorn -c gunicorn_config.py app:app' > /app/start.sh && \
    chmod +x /app/start.sh

# Run with startup script
CMD ["/app/start.sh"]
