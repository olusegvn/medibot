#!/bin/bash

# This script helps run both the backend and frontend of the Medibot application

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not found. Please install Python 3."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is required but not found. Please install Node.js."
    exit 1
fi

echo "Setting up and starting the Flask backend..."
cd api
# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate || source venv/bin/activate.sh

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Start Flask server in the background
echo "Starting Flask server..."
python app.py &
FLASK_PID=$!

# Go back to project root
cd ..

# Install npm dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "Installing npm dependencies..."
    npm install
fi

# Start React app
echo "Starting React app..."
npm run dev

# When the React app is terminated, also terminate the Flask server
echo "Shutting down Flask server..."
kill $FLASK_PID

echo "Application shutdown complete."