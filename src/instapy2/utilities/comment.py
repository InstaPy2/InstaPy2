from .persistence.comment import CommentPersistence
from ..types import FetchMode
from .utility import Utility

from random import choice
from datetime import datetime

class Comment:
    def __init__(self, utility: Utility):
        self.utility = utility
        self.comment_persistence = CommentPersistence(utility=self.utility)

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

        # fetch all comments from persistence:
        comments = self.comment_persistence.get_all_comments()
        print(f"Found {len(comments)} comments in database: {comments}")
        total_posts = 0
        commented_posts = 0
        for index, hashtag in enumerate(iterable=iterable):
            print(f"Fetching posts for hashtag: {hashtag} at index: {index}")
            
            posts = hashtags_medias(name=hashtag, amount=amount)
            total_posts += len(posts)
            for index, post in enumerate(iterable=posts):
                # Catch only FeedbackRequiredException, in cases where comments are disabled
                try:
                    print(f"Commenting on post with id: {post.id} at index: {index}")
                    comment_text = choice(seq=self.comments)
                    if self.utility.client.media_comment(media_id=post.id, text=comment_text):
                        commented_posts += 1
                        print(f"Successfully commented \"{comment_text}\" on post with id: {post.id}")
                        try:
                            self.comment_persistence.insert_comment(post_id=post.id, timestamp=datetime.now(), text=comment_text)
                        except Exception as e:
                            print(f"Error inserting comment into database: {e}")
                except Exception as e:
                    print(f"Error commenting on post with id: {post.id}: {e}")
        print(f"Commented on {commented_posts} out of {total_posts} available posts")