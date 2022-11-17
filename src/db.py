import sqlite3

def get_db():
    db = sqlite3.connect('database.db', check_same_thread=False)
    db.row_factory = sqlite3.Row
    return db


    # db = connection.cursor()
