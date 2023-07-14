from instagrapi import Client

from ..types import FetchMode

class Like:
    def __init__(self, client: Client):
        self.client = client
    
    def hashtags(self, amount: int = 10, iterable: list[str] = None, mode: FetchMode = FetchMode.RECENT):
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


    def locations(self, amount: int = 10, iterable: list[str] = None, mode: FetchMode = FetchMode.RECENT):
        pass

    def usernames(self, amount: int = 10, iterable: list[str] = None):
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

            user_id = self.client.user_id_from_username(username=username)
            posts = self.client.user_medias(user_id=user_id, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                print(f"Liking post with id: {post.id} at index: {index}")

                liked = self.client.media_like(media_id=post.id)
                if liked:
                    liked_posts += 1

        print(f"Liked {liked_posts} out of {total_posts} available posts")