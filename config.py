from decouple import config
from telethon import TelegramClient


PHONE = config('PHONE')
API_ID = config('API_ID')
API_HASH = config('API_HASH')

client = TelegramClient(f"sessions/{PHONE}", api_id=API_ID, api_hash=API_HASH)
