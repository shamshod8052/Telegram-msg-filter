from decouple import config
from pyrogram import Client


PHONE = config('PHONE')
API_ID = config('API_ID')
API_HASH = config('API_HASH')

app = Client(F"sessions/{PHONE}", api_id=API_ID, api_hash=API_HASH)
