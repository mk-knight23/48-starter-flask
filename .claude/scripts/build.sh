#!/bin/bash
# Production build script

set -e

echo "🏗️  Building Flask Starter for production..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Frontend build
echo "⚛️  Building React frontend..."
npm run build

# Backend tests
echo "🧪 Running tests..."
pytest

echo ""
echo "✅ Build complete!"
echo ""
echo "To deploy:"
echo "  gunicorn -c gunicorn_config.py app:app"
