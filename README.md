# Tele-Resolver

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-21%2B-26A5E4?style=flat-square&logo=telegram)
![SQLModel](https://img.shields.io/badge/SQLModel-ORM-red?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-local-003B57?style=flat-square&logo=sqlite)
![uv](https://img.shields.io/badge/uv-package%20manager-blueviolet?style=flat-square)

## Status

![Version](https://img.shields.io/badge/version-0.0.0-blue?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/chris-kechagias/tele-resolver?style=flat-square)
![Commits](https://img.shields.io/github/commit-activity/m/chris-kechagias/tele-resolver?style=flat-square&label=Activity)
![License](https://img.shields.io/github/license/chris-kechagias/tele-resolver?style=flat-square)
![In Progress](https://img.shields.io/badge/status-in%20progress-orange?style=flat-square)

---

## About

A Telegram bot service that acts as a frontend for the [Simple Chatbot API](https://github.com/chris-kechagias/simple-chatbot-api). Handles per-user OpenAI key management and routes messages through the chatbot's streaming backend. Part of a larger portfolio project —> built incrementally, PR by PR.

**Phases:**
- Phase 1 — Scaffold, per-user key storage, basic message routing
- Phase 2 — Streaming responses, conversation context, prompt selection
- Phase 3 — Connect to retail inventory data via the chatbot API

---

## Project Structure

```
tele-resolver/
├── main.py                  # App launcher
├── app/
│   ├── bot.py               # Telegram application setup and run()
│   ├── core/                # Config and database engine
│   ├── handlers/            # Command and message handlers
│   ├── models/              # SQLModel schemas (TelegramUser)
│   └── services/            # Chatbot API client
```

---

## Installation

> Coming soon.

---

## Author

**Chris Kechagias**

[![Medium Badge](https://img.shields.io/badge/@ck.chris.kechagias-black?style=flat&logo=medium&logoColor=white&link=https://medium.com/@ck.chris.kechagias)](https://medium.com/@ck.chris.kechagias)<br>
[![GitHub](https://skillicons.dev/icons?i=github)](https://github.com/chris-kechagias)<br>
[![LinkedIn](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/in/chkechagias)<br>
[![dev.to](https://skillicons.dev/icons?i=devto)](https://dev.to/kris_k)<br>

*Transitioning from retail operations to AI engineering.*

**⭐ If you find this project helpful, consider giving it a star!**
