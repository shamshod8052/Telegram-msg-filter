from typing import Union, List
from info import CHANNELS_INFO


class MessageManager:
    def __init__(self, event):
        self.event = event
        self.text = self.get_text()

    def get_text(self):
        if not (self.event and self.event.message):
            return None
        if getattr(self.event.message, 'text', None):
            return self.event.message.text.lower()
        if getattr(self.event.message, 'caption', None):
            return self.event.caption.lower()
        return None

    @staticmethod
    async def check(text, parts_of_texts: List[List[str]]):
        return any(
            [
                all(
                    [
                        t in text for t in part_of_texts
                    ]
                ) for part_of_texts in parts_of_texts
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
               and await self.check(self.text, channel.parts_of_texts)
               and not await self.check(self.text, channel.not_parts_of_texts)
        ]
