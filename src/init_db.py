import sqlite3

db = sqlite3.connect('database.db')

if not db:
    with open('src/schema.sql') as f:
        db.executescript(f.read())
    
cur = db.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('yang', 'yang')
            )

db.commit()
db.close()