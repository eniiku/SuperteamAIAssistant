from bot import TelegramBot
from config import Config
from llm import LocalLLM


def main():
    config = Config()
    llm = LocalLLM(config)
    bot = TelegramBot(config, llm)
    bot.run()


if __name__ == "__main__":
    main()
