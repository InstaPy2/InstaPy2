from instagrapi import Client

from ..types import FetchMode

class Like:
    def __init__(self, client: Client):
        self.client = client
    
    def hashtags(self, amount: int = 10, iterable: list[str] = None, mode: FetchMode = FetchMode.RECENT):
        pass

    def locations(self, amount: int = 10, iterable: list[str] = None, mode: FetchMode = FetchMode.RECENT):
        pass

    def usernames(self, amount: int = 10, iterable: list[str] = None):
        pass