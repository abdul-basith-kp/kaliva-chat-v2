
import mysql.connector
import os
from dotenv import load_dotenv
from exceptions import DatabaseConnectionError
from logging_config import logger

load_dotenv()
logger.info('testing the logger')
class Database:

    def __init__(self) -> None:
        self.create_tables()

    def create_tables(self) -> None:
        with self.get_database_connection() as conn:
            cur = conn.cursor()
            self.create_users_table(cur)
            self.create_messages_table(cur)
            conn.commit()

    def get_database_connection(self) -> mysql.connector:
        try:
            return mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE') 
            )
        except Exception as e:
            logger.exception('Error occured while connecting to database')
            raise DatabaseConnectionError(f"Failed to connect to Database :: {str(e)}")

    def create_users_table(self, cur) -> None:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(64) NOT NULL UNIQUE,
            password_hash VARCHAR(512) NOT NULL,
            status VARCHAR(16) 
                CHECK (status IN ('ACTIVE', 'DELETED', 'SUSPENDED'))
                DEFAULT 'ACTIVE',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")

    def create_messages_table(self, cur) -> None:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id INT PRIMARY KEY AUTO_INCREMENT,
            sender_id INT NOT NULL,
            receiver_id INT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (sender_id) REFERENCES users(id),
                FOREIGN KEY (receiver_id) REFERENCES users(id)
        )""")

