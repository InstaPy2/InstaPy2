from .persistence import Persistence

from datetime import datetime

class CommentPersistence(Persistence):
    def insert_comment(self, post_id: str, timestamp: datetime):
        query = "INSERT INTO comments (postID, timestamp) VALUES (?, ?)"
        params = (post_id, timestamp.isoformat())
        self._execute_query(query, params)

    def get_all_comments(self):
        query = "SELECT * FROM comments"
        return self.cursor.execute(query).fetchall()