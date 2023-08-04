from .persistence import Persistence

from datetime import datetime

class LikePersistence(Persistence):
    def insert_like(self, post_id: str, timestamp: datetime):
        query = "INSERT INTO likes (postID, timestamp) VALUES (?, ?)"
        params = (post_id, timestamp.isoformat())
        self._execute_query(query, params)

    def get_all_likes(self):
        query = "SELECT * FROM likes"
        return self.cursor.execute(query).fetchall()