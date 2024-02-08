from .logging import Logging
from .openai import OpenAI

from instagrapi import Client
from instagrapi.types import Media, User


class Utility:
    def __init__(self, client: Client, logging: Logging):
        self.client = client
        self.logging = logging

        self.openai = OpenAI()

    def __get_pk(self, query: str) -> int | None:
        places = self.client.fbsearch_places(query=query)
        place_tuple = [
            (place.name, place.city, place.zip, place.pk) for place in places
        ]

        for index, place in enumerate(iterable=place_tuple):
            name, city, zip, pk = place
            selection_string = ""
            for index, element in enumerate(iterable=[name, city, zip, pk]):
                if element is not None and element != "":
                    selection_string += f"{element}" if index == 0 else f", {element}"
            print(f"{index + 1}: {selection_string}")

        selection = int(
            input(f"Enter the index for the correct location (1-{len(place_tuple)}): ")
        )
        if 1 <= selection <= len(places):
            _, _, _, pk = place_tuple[selection - 1]
            return pk
        else:
            return None

    def passes_validation(
        self,
        media: Media,
        comments_range: tuple[int, int],
        followers_range: tuple[int, int],
    ) -> bool:
        username = media.user.username
        if username:
            user_info = self.client.user_info_by_username(username=username)
            return self.__comments_within_range(
                media=media, range=comments_range
            ) and self.__followers_within_range(user=user_info, range=followers_range)
        else:
            return False

    def __comments_within_range(self, media: Media, range: tuple[int, int]) -> bool:
        min, max = range
        return min <= (media.comment_count or 0) <= max

    def __followers_within_range(self, user: User, range: tuple[int, int]) -> bool:
        min, max = range
        return min <= user.follower_count <= max
