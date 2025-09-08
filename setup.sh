#!/bin/bash

# Project Viktor - Professional Setup Script
# Creates virtual environment and installs dependencies

echo "🚀 Project Viktor - Professional Setup"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    echo "   Please install Python 3.8+ and try again"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment
echo "🔧 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "   Virtual environment already exists"
else
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment created successfully"
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing project dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the demo:"
echo "   ./start_demo.sh"
echo ""
echo "To manually activate the environment:"
echo "   source venv/bin/activate"
echo ""