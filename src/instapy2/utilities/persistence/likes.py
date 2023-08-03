from datetime import datetime
from .persistence import Persistence

class LikePersistence(Persistence):
    def __init__(self, username: str):
        super().__init__(username=username)

    def insert_like(self, post_id: str, timestamp: datetime):
        query = "INSERT INTO likes (postID, timestamp) VALUES (?, ?)"
        params = (post_id, timestamp.isoformat())
        self._execute_query(query, params)

    def get_all_likes(self):
        query = "SELECT * FROM likes"
        return self.cursor.execute(query).fetchall()