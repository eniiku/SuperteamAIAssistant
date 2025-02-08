from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

        
        
