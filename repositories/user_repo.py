

from database import Database


class userRepo:
    def __init__(self, db: Database) -> None:
        self.db = db

    def create_user(self, cur, username: str, password_hash: str) -> None:
        cur.execute("""
        INSERT INTO users
        (username, password_hash)
        VALUES
        (%s, %s)
        """, (username, password_hash))
        