from src.db import get_db
from datetime import datetime

con = get_db()
cur = con.cursor()
# user = cur.execute("SELECT * FROM users WHERE username = ?", ['admin']).fetchone()
# user_id = user['id']
# print(user_id)
# favoMovies = cur.execute('SELECT * FROM favo WHERE user_id = ?', [user_id]).fetchall()
# ids = [(item['favoMovie_id'],) for item in favoMovies]
# print(ids)
# data = []
# for id in ids:
#     cur.execute('SELECT * FROM movies WHERE id = ?', id)
#     data.append(cur.fetchall)
# print(data)

# query = cur.execute('SELECT * FROM movies WHERE cast(rating as float) >= 8.5')
# print(query)
# print(cur.fetchall())
cur.execute('INSERT INTO apicalltime (apiname, time) VALUES (?, ?);', ('intheaters', datetime.now().strftime('%A, %d %b %Y %l:%M %p')))
con.commit()
query = cur.execute("SELECT * FROM apicalltime WHERE apiname = ?", ['intheaters'])
time = query.fetchone()['time']
print(time)
