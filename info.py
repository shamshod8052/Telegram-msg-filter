import json
from pathlib import Path
from typing import Union, List


class Info:
    def __init__(self, chat_id: Union[str, int], parts_of_texts: List[str], not_parts_of_texts: List[str]):
        self.chat_id = chat_id
        self.parts_of_texts = [[text.lower() for text in part_of_texts] for part_of_texts in parts_of_texts]
        self.not_parts_of_texts = [[text.lower() for text in part_of_texts] for part_of_texts in not_parts_of_texts]

with open(Path(__file__).resolve().parent / "channels.json", encoding="utf-8") as f:
    data = json.load(f)

CHANNELS_INFO = [Info(**item) for item in data]
