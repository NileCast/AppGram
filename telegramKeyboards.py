import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Your bot token
TOKEN = '7746812085:AAEK_cc0Xo4a_5aJ5N4hHhyrXvewq9k5r8g'

# Define the Web App URL
WEB_APP_URL = 'https://nilecast.github.io/AppGram/store.html'

# Define keyboard layout with both Install and Share buttons
keyboard = [
    [KeyboardButton("Install", web_app=WebAppInfo(url=WEB_APP_URL))],
    [KeyboardButton("Share")]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcoming message when the command /start is issued."""
    user = update.effective_user
    welcome_message = (
        f"👋 Welcome, {user.mention_html()}! 🎉\n\n"
        "Here's what you can do:\n\n"
        "🔸 Click 'Install' to get our app and start your journey.\n"
        "🔸 Use 'Share' to spread the word and invite your friends!\n\n"
    )
    await update.message.reply_html(
        welcome_message,
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle user messages."""
    text = update.message.text

    if text == 'Share':
        share_message = (
            "🌟 Thanks for sharing NileCast! 🌟\n\n"
            "Here's the link to our awesome app: https://t.me/NileCast_Bot\n\n"
            "Your friends will love it! 😍"
        )
        await update.message.reply_text(share_message, reply_markup=reply_markup)
    else:
        await update.message.reply_text(
            "I'm not sure how to respond to that. Please use the buttons below to interact with me.",
            reply_markup=reply_markup
        )

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()