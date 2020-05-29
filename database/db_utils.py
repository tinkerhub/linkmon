import sqlite3
from sqlite3 import OperationalError
def let_there_be_table():
    create_table = """ 
        CREATE TABLE STORE_URL(
            ID INT PRIMARY KEY AUTOINCREMENT,
            ACT_URL TEXT NOT NULL,
            CUSTOM_URL TEXT NOT NULL
        );
        """
    with sqlite3.connect('database/urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError:
            return "Something went wrong"

let_there_be_table()

