from typing import Union, List
from info import CHANNELS_INFO


class MessageManager:
    def __init__(self, event):
        self.event = event
        self.text = self.get_text()

    def get_text(self):
        if not (self.event and self.event.message):
            return None
        if self.event.message.text:
            return self.event.message.text.lower()
        if self.event.message.caption:
            return self.event.caption.lower()
        return None

    async def check(self, texts):
        return all(
            [
                (t in self.text) for t in texts
            ]
        )

    async def get_chat_ids(self) -> List[Union[int, str]]:
        if not self.text:
            return []
        chat = await self.event.get_chat()
        return [
            channel.chat_id for channel in CHANNELS_INFO
            if channel.chat_id != self.event.chat_id
               and channel.chat_id.lstrip('@') != chat.username
               and await self.check(channel.parts_of_text)
        ]
