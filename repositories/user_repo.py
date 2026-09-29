

from database import Database
from models.user import User


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

    def get_user_by_username(self, cur, username: str) -> User:
        cur.execute("""
        SELECT id, username, password_hash, status, created_at
        FROM users
        WHERE username = %s
        """, (username, ))
        row = cur.fetchone()
        return User(
            *row
        )

    def get_user_by_user_id(self, cur, user_id: int) -> User:
        cur.execute("""
        SELECT id, username, password_hash, status, created_at
        FROM users
        WHERE id = %s
        """, (user_id, ))
        row = cur.fetchone()
        return User(
            *row
        )