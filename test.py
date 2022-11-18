from src.db import get_db

con = get_db()
cur = con.cursor()
user = cur.execute("SELECT * FROM users WHERE username = ?", ['admin']).fetchone()
user_id = user['id']
print(user_id)
favoMovies = cur.execute('SELECT * FROM favo WHERE user_id = ?', [user_id]).fetchall()
ids = [(item['favoMovie_id'],) for item in favoMovies]
print(ids)
data = []
for id in ids:
    cur.execute('SELECT * FROM movies WHERE id = ?', id)
    data.append(cur.fetchall)
print(data)
