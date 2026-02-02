#!/bin/bash
# Flask Starter - Initial Setup Script

set -e

echo "🧊 Setting up Flask Starter..."

# Python setup
echo "📦 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔐 Setting up environment..."
cp .env.example .env

echo "🗄️  Initializing database..."
flask init-db
flask seed-db

echo "📥 Installing Node dependencies..."
npm install

echo "✅ Setup complete!"
echo ""
echo "Backend commands:"
echo "  flask run          # Start Flask server"
echo "  flask routes       # List all routes"
echo ""
echo "Frontend commands:"
echo "  npm run dev        # Start Vite dev server"
echo "  npm run build      # Build for production"
echo ""
echo "Happy coding! 🚀"
