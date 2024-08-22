import os
import logging
from pyrogram import Client
from dotenv import load_dotenv

class katsu:
    def __init__(self):
        self.environment = load_dotenv(".env") 
        self.name = "katsu_Bot"
        self.api_id = os.getenv('API_ID')
        self.api_hash = os.getenv('API_HASH')
        self.bot_token = os.getenv('BOT_TOKEN')
        self.plugins = dict(root = 'plugins')
        
        self.log = logging.basicConfig(level=logging.INFO)
        
    
    def run(self):
        logging.info(f"Starting {self.name}")
        
        _start_ = Client(
                        self.name,
                        api_id = self.api_id,
                        api_hash = self.api_hash,
                        bot_token = self.bot_token,
                        plugins = self.plugins) 
        

        return _start_.run()
    

try: katsu().run()
except Exception as e:...