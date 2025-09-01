from typing import Union, List

CHANNEL_ID = "@OnlyPythonJobs"
NEED_TEXT_PARTS = [
    "python",
]

class Info:
    def __init__(self, chat_id: Union[str, int], parts_of_text: List[str]):
        self.chat_id = chat_id
        self.parts_of_text = [text.lower() for text in parts_of_text]

CHANNELS_INFO = [
    Info(
        "@OnlyPythonJobs",
        ["python"]
    ),
]
