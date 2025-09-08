#!/bin/bash

# Project Viktor Demo Startup Script
# Professional virtual environment approach

echo "🚀 Project Viktor - Physics AI Explorer"
echo "======================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Virtual environment not found. Setting up..."
    echo "   Running setup script..."
    ./setup.sh
    if [ $? -ne 0 ]; then
        echo "❌ Setup failed. Please run ./setup.sh manually"
        exit 1
    fi
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Verify dependencies are installed
echo "🔍 Verifying dependencies..."
python -c "import flask, flask_cors, numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Dependencies missing. Installing..."
    pip install -r requirements.txt
fi

echo "✅ Environment ready"
echo ""

# Start the backend server
echo "🌐 Starting Viktor backend server..."
echo "   Server will be available at: http://localhost:3001"
echo "   Demo UI will be available at: http://localhost:3001"
echo ""
echo "💡 Tips:"
echo "   • Try searching for 'energy' or 'quantum'"
echo "   • Click on formulas in the 3D view"
echo "   • Use the control buttons to explore"
echo ""
echo "🛑 Press Ctrl+C to stop the server"
echo ""

# Start the Python backend
python3 demo_backend.py