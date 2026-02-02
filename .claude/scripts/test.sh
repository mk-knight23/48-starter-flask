#!/bin/bash
# Test script - run all tests with coverage

set -e

echo "🧪 Running Flask Starter test suite..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Backend tests
echo "🐍 Running Python tests..."
pytest -v --cov=app --cov-report=term-missing --cov-report=html

echo ""
echo "✅ Tests complete!"
echo "Coverage report: htmlcov/index.html"
