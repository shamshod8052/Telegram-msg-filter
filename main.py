import asyncio
import traceback

from telethon import events
from telethon.errors import FloodWaitError

from config import client
from manager import MessageManager


async def forward(chat_id, event, n=1):
    if n > 3:
        return
    try:
        await event.forward_to(int(chat_id) if chat_id.lstrip('-').isdigit() else chat_id)
    except FloodWaitError as f:
        print(f"Floodwait {f.seconds} seconds")
        await asyncio.sleep(f.seconds)
        await forward(chat_id, event, n + 1)
    except Exception as e:
        traceback.print_exc()

@client.on(events.NewMessage)
async def my_handler(event: events.NewMessage.Event):
    chat = await event.get_chat()
    if not (chat.broadcast or chat.megagroup or chat.title):
        return

    manager = MessageManager(event)
    chat_ids = await manager.get_chat_ids()
    for chat_id in chat_ids:
        await forward(chat_id, event)


if __name__ == "__main__":
    print("Working...")

    client.start()
    client.run_until_disconnected()
