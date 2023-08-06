from ..types import FetchMode
from .utility import Utility

from random import choice

class Comment:
    def __init__(self, utility: Utility):
        self.utility = utility

        self.comments = [] # list of comments to randomly select from
        self.min_comments = 10 # only comment if posts comments are >=
        self.max_comments = 1000 # only comment if posts comments are <=
        self.min_followers = 10 # only comment if postees follower count is >=
        self.max_followers = 1000 # only comment if postees follower count is <=

    def hashtags(self, amount: int = 10, iterable: list[str] = [], mode: FetchMode = FetchMode.RECENT):
        """
        Comments on up to the `amount` of posts per hashtag in `iterable`

            Parameters
                amount (int): amount of posts to fetch per iterable
                iterable (list[str]): list of hashtags to fetch posts from
        """

        match mode:
            case FetchMode.RECENT:
                hashtags_medias = self.utility.client.hashtag_medias_recent
            case FetchMode.TOP:
                hashtags_medias = self.utility.client.hashtag_medias_top

        total_posts = 0
        commented_posts = 0
        for index, hashtag in enumerate(iterable=iterable):
            print(f"Fetching posts for hashtag: {hashtag} at index: {index}")
            
            posts = hashtags_medias(name=hashtag, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                print(f"Commenting on post with id: {post.id} at index: {index}")

                if self.utility.client.media_comment(media_id=post.id, text=choice(seq=self.comments)):
                    commented_posts += 1

        print(f"Commented on {commented_posts} out of {total_posts} available posts")