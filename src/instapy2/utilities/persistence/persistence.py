from ..utility import Utility

from sqlite3 import connect, Connection

class Persistence:
    def __init__(self, utility: Utility):
        self.utility = utility

        self.db_file_path = f"{self.utility.client.username or "default"}_data.db"
        self.connection = self._open()
        self.cursor = self.connection.cursor()
        self.create_tables()

    def _open(self) -> Connection:
        return connect(database=self.db_file_path)

    def _execute_query(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def _table_exists(self, table: str) -> bool:
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        result = self.cursor.execute(query, (table,)).fetchone()
        return result is not None

    def create_tables(self):
        # Create the comments table, which contains columns for a postID and a timestamp
        if not self._table_exists(table="comments"):
            query = "CREATE TABLE comments (postID TEXT, timestamp TEXT)"
            self._execute_query(query=query)
        # Create the like table, which contains columns for a postID and a timestamp
        if not self._table_exists(table="likes"):
            query = "CREATE TABLE likes (postID TEXT, timestamp TEXT)"
            self._execute_query(query=query)

    def close(self):
        self.cursor.close()
        self.connection.close()
