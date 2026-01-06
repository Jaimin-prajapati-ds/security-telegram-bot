#!/usr/bin/env python3
"""
Security Telegram Bot - Main Entry Point
Powerful ethical cybersecurity bot with alerts, logging, and monitoring capabilities

Usage:
    python3 src/bot_main.py

Author: Jaimin Prajapati
Version: 1.0.0
"""

import os
import sys
import asyncio
import logging
from pathlib import Path
from datetime import datetime

try:
    from telegram import Update, BotCommand
    from telegram.ext import (
        Application,
        CommandHandler,
        MessageHandler,
        filters,
        ContextTypes,
    )
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Missing dependencies: {e}")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "0").split(",")))

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN not found in .env file")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SecurityBot:
    """Main Security Telegram Bot Class"""

    def __init__(self, token: str, admin_ids: list):
        self.token = token
        self.admin_ids = admin_ids
        self.app = None
        self.alerts = []
        self.start_time = datetime.now()

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        welcome_text = f"""
🤖 **Security Telegram Bot**

Hello {user.first_name}! I'm your cybersecurity assistant.

📋 **Available Commands:**
/start - Initialize bot
/help - Show help message
/status - Check bot and server status
/alerts - View recent security alerts
/logs - Query logs (usage: /logs ssh 50)
/scan - Trigger security scan
/explain - Explain an alert

🔐 **Security First:**
All operations are logged and authorized users only.
        """
        await update.message.reply_text(welcome_text, parse_mode="Markdown")
        logger.info(f"User {user.id} started bot")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
**Commands:**
• `/start` - Start the bot
• `/status` - Show bot status
• `/alerts` - Recent alerts (admin only)
• `/logs <type> [count]` - View logs (ssh, web, app)
• `/scan <target>` - Scan target (admin only)
• `/explain <id>` - Explain alert
• `/help` - This message

**Examples:**
`/logs ssh 20` - Last 20 SSH logs
`/scan 192.168.1.100` - Scan server
        """
        await update.message.reply_text(help_text, parse_mode="Markdown")

    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /status command"""
        uptime = datetime.now() - self.start_time
        status_text = f"""
✅ **Bot Status**

🔋 Uptime: {uptime}
🚀 Version: 1.0.0
📊 Alerts: {len(self.alerts)}
👤 User: {update.effective_user.first_name}
⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        await update.message.reply_text(status_text, parse_mode="Markdown")
        logger.info(f"Status check by {update.effective_user.id}")

    async def alerts_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /alerts command (admin only)"""
        if update.effective_user.id not in self.admin_ids:
            await update.message.reply_text("❌ Access Denied")
            return

        if not self.alerts:
            await update.message.reply_text(
                "✅ No alerts at the moment. System is secure."
            )
            return

        alerts_text = "🔴 **Recent Alerts:**\n\n"
        for alert in self.alerts[-10:]:  # Last 10 alerts
            alerts_text += f"• {alert}\n"

        await update.message.reply_text(alerts_text, parse_mode="Markdown")
        logger.info(f"Alerts viewed by admin {update.effective_user.id}")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular messages"""
        user_message = update.message.text
        logger.info(f"Message from {update.effective_user.id}: {user_message[:50]}")

        if "security" in user_message.lower():
            await update.message.reply_text(
                "🛡️ Security is our priority! Use /help for available commands."
            )

    async def initialize_commands(self):
        """Register bot commands"""
        commands = [
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Show help message"),
            BotCommand("status", "Check bot status"),
            BotCommand("alerts", "View alerts (admin)"),
            BotCommand("logs", "Query logs"),
            BotCommand("scan", "Security scan"),
        ]
        await self.app.bot.set_my_commands(commands)
        logger.info("Bot commands initialized")

    async def setup(self):
        """Setup bot application"""
        self.app = Application.builder().token(self.token).build()

        # Register handlers
        self.app.add_handler(CommandHandler("start", self.start_command))
        self.app.add_handler(CommandHandler("help", self.help_command))
        self.app.add_handler(CommandHandler("status", self.status_command))
        self.app.add_handler(CommandHandler("alerts", self.alerts_command))
        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
        )

        logger.info("Bot handlers registered")

    async def run(self):
        """Run the bot"""
        await self.setup()
        await self.initialize_commands()

        logger.info("Starting Security Telegram Bot...")
        print("🤖 Bot is running. Press Ctrl+C to stop.")

        async with self.app:
            await self.app.start()
            await self.app.updater.start_polling()
            try:
                await asyncio.Event().wait()  # Keep running
            except KeyboardInterrupt:
                logger.info("Bot stopped by user")
            finally:
                await self.app.updater.stop()
                await self.app.stop()


def main():
    """Main entry point"""
    print("\n" + "="*50)
    print("🤖 Security Telegram Bot v1.0.0")
    print("="*50 + "\n")

    bot = SecurityBot(BOT_TOKEN, ADMIN_IDS)
    asyncio.run(bot.run())


if __name__ == "__main__":
    main()
