import sqlite3

DATABASE_PATH = "automotive.db"


def get_connection():
    return sqlite3.connect(
        DATABASE_PATH
    )