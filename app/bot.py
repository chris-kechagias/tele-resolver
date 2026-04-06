import logging

from telegram.ext import ApplicationBuilder

from app.core.config import config
from app.core.database import init_db

logger = logging.getLogger(__name__)


def run() -> None:
    """Start the Telegram bot using long polling."""
    init_db()

    app = ApplicationBuilder().token(config.telegram_bot_token).build()

    # Handlers will be registered here

    logger.info("Bot is running...")
    app.run_polling()
