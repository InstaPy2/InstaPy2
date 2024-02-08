from instagrapi.types import Media

from enum import StrEnum
from random import choice
from requests import post

class CompletionModel(StrEnum):
    TEXT_DAVINCI003 = "text-davinci-003"

class Completions:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.model = CompletionModel.TEXT_DAVINCI003
        self.prompts = []

    def completion_for_media(self, media: Media) -> str:
        response_json = post(url="https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization" : f"Bearer {self.api_key}",
                "Content-Type" : "application/json"
            },
            data={
                "model" : self.model,
                "prompt" : choice(seq=self.prompts) + f": {media.caption_text}"
            }
        ).json()
        return choice(seq=response_json["choices"])