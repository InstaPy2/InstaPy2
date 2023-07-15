from .utility import Utility
from ..types import FetchMode

class Like:
    def __init__(self, utility: Utility):
        self.utility = utility
    
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
                hashtags_medias = self.utility.client.hashtag_medias_recent
            case FetchMode.TOP:
                hashtags_medias = self.utility.client.hashtag_medias_top

        total_posts = 0
        liked_posts = 0
        for index, hashtag in enumerate(iterable=iterable):
            print(f"Fetching posts for hashtag: {hashtag} at index: {index}")

            
            posts = hashtags_medias(name=hashtag, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                print(f"Liking post with id: {post.id} at index: {index}")

                liked = self.utility.client.media_like(media_id=post.id)
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
                location_medias = self.utility.client.location_medias_recent
            case FetchMode.TOP:
                location_medias = self.utility.client.location_medias_top

        total_posts = 0
        liked_posts = 0
        for index, location in enumerate(iterable=iterable):
            print(f"Fetching posts for location: {location} at index: {index}")

            location_pk = self.utility.__get_pk(query=location)
            if location_pk:
                posts = location_medias(location_pk=location_pk, amount=amount)
                total_posts += len(posts)
                for index, post in enumerate(iterable=posts):
                    print(f"Liking post with id: {post.id} at index: {index}")

                    liked = self.utility.client.media_like(media_id=post.id)
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

            user_id = int(self.utility.client.user_id_from_username(username=username))
            posts = self.utility.client.user_medias(user_id=user_id, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                print(f"Liking post with id: {post.id} at index: {index}")

                liked = self.utility.client.media_like(media_id=post.id)
                if liked:
                    liked_posts += 1

        print(f"Liked {liked_posts} out of {total_posts} available posts")