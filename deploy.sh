#!/bin/bash

# Security Telegram Bot - Deployment Script
# This script automates the setup and deployment of the security telegram bot
# Usage: bash deploy.sh [dev|prod]

set -e  # Exit on error

echo "======================================="
echo "Security Telegram Bot - Deployment"
echo "======================================="

# Configuration
ENV=${1:-dev}
BOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
LOGS_DIR="$BOT_DIR/logs"
VENV_DIR="$BOT_DIR/venv"

echo "\n[*] Environment: $ENV"
echo "[*] Bot Directory: $BOT_DIR"

# Create logs directory
echo "\n[*] Creating logs directory..."
mkdir -p "$LOGS_DIR"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "[*] Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    echo "[+] Virtual environment created"
else
    echo "[+] Virtual environment already exists"
    source "$VENV_DIR/bin/activate"
fi

# Install dependencies
echo "\n[*] Installing dependencies..."
pip install --upgrade pip
pip install -r "$BOT_DIR/requirements.txt"
echo "[+] Dependencies installed"

# Configure environment
echo "\n[*] Configuring environment..."
if [ ! -f "$BOT_DIR/.env" ]; then
    echo "[!] .env file not found. Creating from template..."
    cp "$BOT_DIR/.env.example" "$BOT_DIR/.env"
    echo "[*] Please edit .env file with your configuration"
    echo "[*] Especially set BOT_TOKEN and ADMIN_IDS"
    exit 1
else
    echo "[+] .env file exists"
fi

# Run bot based on environment
echo "\n[*] Starting Security Telegram Bot..."
echo "[*] Environment: $ENV"

if [ "$ENV" = "dev" ]; then
    echo "[*] Running in development mode"
    python3 "$BOT_DIR/src/bot_main.py"
elif [ "$ENV" = "prod" ]; then
    echo "[*] Running in production mode"
    echo "[*] Consider using systemd or screen for background execution"
    nohup python3 "$BOT_DIR/src/bot_main.py" >> "$LOGS_DIR/bot.log" 2>&1 &
    echo "[+] Bot started in background. PID: $!"
else
    echo "[!] Invalid environment. Use 'dev' or 'prod'"
    exit 1
fi

echo "\n[+] Deployment complete!"
echo "\n======================================="
