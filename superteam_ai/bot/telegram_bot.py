import asyncio  # new import

from superteam_ai.config import Config
from superteam_ai.llm.local_llm import LocalLLM
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters


class TelegramBot:
    def __init__(self, config, llm):
        self.config = config
        self.llm = llm
        self.application = Application.builder().token(config.TELEGRAM_TOKEN).build()
        self._setup_handlers()

    def _setup_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
        )

    async def start(self, update: Update, context):
        await update.message.reply_text(
            "Hello!🙋‍♂️ I am the official superteam Vietnam Chatbot, I was created by Eniiku & eskayML, Let me Answer all your questions!"
        )

    async def handle_message(self, update: Update, context):
        user_message = update.message.text
        # Run conversation_turn in a thread to avoid blocking the event loop
        response = await asyncio.to_thread(self.llm.conversation_turn, user_message)
        await update.message.reply_text(response)

    def run(self):
        self.application.run_polling()


if __name__ == "__main__":
    config = Config()
    llm_config = {
        "model_name": "deepseek-r1:1.5b",
        "embedding_model_name": "nomic-embed-text",
        "vector_store_path": "./vector_store",
    }
    llm = LocalLLM(llm_config)
    llm.load_documents(["./data/sample.pdf"])
    bot = TelegramBot(config, llm)
    bot.run()
