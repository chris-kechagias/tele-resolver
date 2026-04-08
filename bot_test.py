"""
Minimal test bot — local only, no auth, no database.

Wires Telegram messages directly to the chatbot API via long polling.
Each message starts a fresh conversation. No key management, no persistence.
"""

import json
import logging

import httpx
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from app.core.config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Greet the user."""
    await update.message.reply_text(
        "Hey! I'm your chatbot. Send me a message to get started."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Forward the message to the chatbot API and reply with the response."""
    user_text = update.message.text

    payload = {
        "user_id": config.test_user_id,
        "user_message": user_text,
    }

    try:
        async with httpx.AsyncClient(timeout=60.0, follow_redirects=True) as client:
            response = await client.post(
                f"{config.chatbot_api_url}/chat",
                json=payload,
            )
            response.raise_for_status()

            # Parse the SSE stream and collect the full response text
            full_text = ""
            for line in response.text.splitlines():
                if line.startswith("data:"):
                    data = line[5:].strip()
                    if data == "[DONE]":
                        break
                    chunk = json.loads(data)
                    if "content" in chunk:
                        full_text += chunk["content"]

        await update.message.reply_text(full_text or "No response received.")

    except Exception as e:
        logger.error(f"Chatbot API error: {e}")
        await update.message.reply_text("Something went wrong. Try again.")


def run():
    app = ApplicationBuilder().token(config.telegram_bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Test bot running...")
    app.run_polling()


if __name__ == "__main__":
    run()
