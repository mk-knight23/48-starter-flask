#!/bin/bash
# Development script - run both frontend and backend

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🧊 Flask Starter - Development Mode${NC}"
echo ""

# Activate virtual environment
source venv/bin/activate

# Start Flask backend in background
echo -e "${GREEN}📡 Starting Flask backend...${NC}"
flask run &
BACKEND_PID=$!

# Wait a moment
sleep 2

# Start Vite frontend
echo -e "${GREEN}⚛️  Starting Vite frontend...${NC}"
npm run dev &
FRONTEND_PID=$!

echo ""
echo -e "${BLUE}✨ Both servers running!${NC}"
echo "  Backend:  http://localhost:5000"
echo "  Frontend: http://localhost:5173"
echo "  API Docs: http://localhost:5000/api/v1/docs"
echo ""
echo "Press Ctrl+C to stop both servers"

# Handle Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT

# Wait for both processes
wait
