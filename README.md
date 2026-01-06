# Security Telegram Bot 🤖

A powerful, ethical cybersecurity Telegram bot with real-time alerts, log monitoring, and automated security intelligence for defensive security operations.

## 🎯 Features

### Core Security Features
- **Real-time Log Monitoring**: Watch SSH, web server, and application logs
- **Alert Engine**: Configurable rules for detecting suspicious activities
- **Threat Intelligence**: Automated analysis and reporting
- **Vulnerability Alerts**: Integration with security scanning tools
- **Log Analysis**: Parse and analyze security logs with AI insights

### Bot Commands
- `/start` - Initialize bot and get welcome message
- `/status` - Check bot and server status
- `/alerts` - View recent security alerts
- `/logs` - Query filtered logs (SSH, web, app)
- `/scan` - Trigger security scan on authorized targets
- `/explain <alert_id>` - Get AI explanation of alert
- `/help` - List all available commands

## 📋 Project Structure

```
security-telegram-bot/
├── config/
│   ├── config.example.yaml
│   └── rules.yaml
├── src/
│   ├── bot_main.py              # Main bot entry point
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── command_handlers.py  # /start, /help, etc.
│   │   ├── alert_handlers.py    # Alert-related commands
│   │   └── admin_handlers.py    # Admin-only operations
│   ├── security/
│   │   ├── log_watcher.py       # Monitor log files
│   │   ├── rules_engine.py      # Alert rules evaluation
│   │   ├── threat_analyzer.py   # AI-based threat analysis
│   │   └── scanners.py          # Integration with security tools
│   └── db/
│       ├── models.py            # Database models
│       └── repository.py        # Data access layer
├── scripts/
│   ├── deploy.sh
│   ├── monitor.sh
│   └── setup.sh
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Telegram Bot Token (from BotFather)
- Linux server (for monitoring) or VPS

### Installation

```bash
# Clone repository
git clone https://github.com/Jaimin-prajapati-ds/security-telegram-bot.git
cd security-telegram-bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure bot
cp config/config.example.yaml config/config.yaml
# Edit config.yaml with your settings

# Set environment variables
cp .env.example .env
# Edit .env with your Telegram token

# Run bot
python3 src/bot_main.py
```

## ⚙️ Configuration

Edit `config/config.yaml`:

```yaml
bot:
  token: "YOUR_BOT_TOKEN_HERE"
  admin_ids: [123456789]

logging:
  ssh_log: "/var/log/auth.log"
  web_log: "/var/log/apache2/access.log"

alerts:
  enabled: true
  failed_login_threshold: 5
  rate_limit_check: true
```

## 🔐 Security Considerations

✅ **For Defensive Use Only**: This bot is designed for legitimate security operations and monitoring of systems you own or manage.

✅ **Ethical Standards**: 
- All operations are logged
- Admin-only sensitive commands
- No unauthorized access
- Proper authentication required

✅ **Best Practices**:
- Use in private/authorized networks only
- Secure your bot token in `.env` file
- Restrict admin access
- Regular log reviews
- Monitor for abuse

## 📊 Alert Types

| Type | Example | Severity |
|------|---------|----------|
| SSH Brute Force | 5+ failed logins in 10 min | 🔴 High |
| Suspicious URL | Malicious domain detected | 🔴 High |
| Rate Limiting | 100+ requests/min | 🟡 Medium |
| New User Login | SSH from new IP | 🟠 Medium |
| Log Anomaly | Unusual pattern detected | 🟡 Low |

## 🤝 Contributing

Fork this repository, create a feature branch, and submit a pull request.

```bash
git checkout -b feature/new-feature
git commit -m 'Add new feature'
git push origin feature/new-feature
```

## 📜 License

MIT License - See LICENSE file for details

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: jaimin@example.com

---

**⚠️ Disclaimer**: This tool is for defensive security purposes only. Unauthorized access to computer systems is illegal. Always obtain proper authorization before deploying this bot.

**Made with ❤️ by Jaimin Prajapati**
