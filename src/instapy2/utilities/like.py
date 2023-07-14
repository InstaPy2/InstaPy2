from instagrapi import Client

from ..types import FetchMode

class Like:
    def __init__(self, client: Client):
        self.client = client

    def __get_pk(self, location: str) -> int | None:
        places = self.client.fbsearch_places(query=location)
        place_tuple = [(place.name, place.city, place.zip, place.pk) for place in places]

        for index, place in enumerate(iterable=place_tuple):
            name, city, zip, pk = place
            selection_string = ""
            if name is not None and name != "":
                selection_string += name
            if city is not None and city != "":
                selection_string += f", {city}"
            if zip is not None and zip != "":
                selection_string += f", {zip}"
            print(f"{index + 1}: {selection_string}")

        selection = int(input(f"Enter the index for the correct location (1-{len(place_tuple)}): "))

        if 1 <= selection <= len(places):
            _, _, _, pk = place_tuple[selection - 1]
            return pk
        else:
            return None
    
    def hashtags(self, amount: int = 10, iterable: list[str] = [], mode: FetchMode = FetchMode.RECENT):
        """
        Likes up to the `amount` of posts per hashtag in `iterable` searched by `mode`

            Parameters
                amount (int): amount of posts to fetch per iterable
                iterable (list[str]): list of hashtags to fetch posts from
                mode (FetchMode): mode to use when fetching posts
        """
        
        match mode:
            case FetchMode.RECENT:
                hashtags_medias = self.client.hashtag_medias_recent
            case FetchMode.TOP:
                hashtags_medias = self.client.hashtag_medias_top

        total_posts = 0
        liked_posts = 0
        for index, hashtag in enumerate(iterable=iterable):
            print(f"Fetching posts for hashtag: {hashtag} at index: {index}")

            
            posts = hashtags_medias(name=hashtag, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                print(f"Liking post with id: {post.id} at index: {index}")

                liked = self.client.media_like(media_id=post.id)
                if liked:
                    liked_posts += 1

        print(f"Liked {liked_posts} out of {total_posts} available posts")


    def locations(self, amount: int = 10, iterable: list[str] = [], mode: FetchMode = FetchMode.RECENT):
        """
        Likes up to the `amount` of posts per location in `iterable` searched by `mode`

            Parameters
                amount (int): amount of posts to fetch per iterable
                iterable (list[str]): list of locations to fetch posts from
                mode (FetchMode): mode to use when fetching posts
        """

        match mode:
            case FetchMode.RECENT:
                location_medias = self.client.location_medias_recent
            case FetchMode.TOP:
                location_medias = self.client.location_medias_top

        total_posts = 0
        liked_posts = 0
        for index, location in enumerate(iterable=iterable):
            print(f"Fetching posts for location: {location} at index: {index}")

            location_pk = self.__get_pk(location=location)
            if location_pk:
                posts = location_medias(location_pk=location_pk, amount=amount)
                total_posts += len(posts)
                for index, post in enumerate(iterable=posts):
                    print(f"Liking post with id: {post.id} at index: {index}")

                    liked = self.client.media_like(media_id=post.id)
                    if liked:
                        liked_posts += 1
            else:
                print("Invalid location pk selected. Please select a valid one")
                exit(1) # exit() or break?

        print(f"Liked {liked_posts} out of {total_posts} available posts")



    def usernames(self, amount: int = 10, iterable: list[str] = []):
        """
        Likes up to the `amount` of posts per username in `iterable`

            Parameters
                amount (int): amount of posts to fetch per iterable
                iterable (list[str]): list of usernames to fetch posts from
        """
        
        total_posts = 0
        liked_posts = 0
        for index, username in enumerate(iterable=iterable):
            print(f"Fetching posts for username: {username} at index: {index}")

            user_id = int(self.client.user_id_from_username(username=username))
            posts = self.client.user_medias(user_id=user_id, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                print(f"Liking post with id: {post.id} at index: {index}")

                liked = self.client.media_like(media_id=post.id)
                if liked:
                    liked_posts += 1

        print(f"Liked {liked_posts} out of {total_posts} available posts")