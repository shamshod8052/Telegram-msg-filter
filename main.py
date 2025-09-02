import asyncio
import traceback

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from config import app
from manager import MessageManager


async def forward(chat_id, message, n=1):
    if n > 3:
        return
    try:
        await message.forward(chat_id)
    except FloodWait as f:
        print(f"Floodwait {f.value} seconds")
        await asyncio.sleep(f.value)
        await forward(chat_id, message, n + 1)
    except Exception as e:
        traceback.print_exc()

@app.on_message()
async def my_handler(client, message):
    if message.chat.type not in [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.CHANNEL]:
        return

    manager = MessageManager(message)
    for chat_id in manager.get_chat_ids():
        await forward(chat_id, message)


if __name__ == "__main__":
    print("Working...")
    app.run()
