from .utility import Utility

class Comment:
    def __init__(self, utility: Utility):
        self.utility = utility

        self.min_comments = 10 # only comment if posts comments are >=
        self.max_comments = 1000 # only comment if posts comments are <=
        self.min_followers = 10 # only comment if postees follower count is >=
        self.max_followers = 1000 # only comment if postees follower count is <=