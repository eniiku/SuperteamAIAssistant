from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)


class TelegramBot:
    def __init__(self, config, llm):
        self.config = config
        self.llm = llm
        self.updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self._setup_handlers()

    def _setup_handlers(self):
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.handle_message))

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text("Hello! I am your assistant.")

    def handle_message(self, update: Update, context: CallbackContext):
        user_message = update.message.text
        response = self.llm.generate_response(user_message)
        update.message.reply_text(response)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
