from typing import Union, List
from info import CHANNELS_INFO


class MessageManager:
    def __init__(self, message):
        self.message = message
        self.text = self.get_text()

    def get_text(self):
        if self.message.text:
            return self.message.text.lower()
        if self.message.caption:
            return self.message.caption.lower()
        return None

    def check(self, texts):
        return all(
            [
                (t in self.text) for t in texts
            ]
        )

    def get_chat_ids(self) -> List[Union[int, str]]:
        if not self.text:
            return []
        return [
            channel.chat_id for channel in CHANNELS_INFO
            if channel.chat_id != self.message.chat.id
               and channel.chat_id.lstrip('@') != self.message.chat.username
               and self.check(channel.parts_of_text)
        ]
