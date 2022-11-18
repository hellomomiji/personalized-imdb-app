from src.db import get_db
from datetime import datetime

con = get_db()
cur = con.cursor()

def recordApiCallTime(apiname):
    now = datetime.now().strftime('%A, %d %b %Y %l:%M %p')
    query = cur.execute('SELECT * FROM apicalltime WHERE apiname = ?', [apiname]).fetchone()
    if not query:
        cur.execute('INSERT INTO apicalltime (apiname, time) VALUES (?, ?);', (apiname, now))
        con.commit()
        print("Inserted api call time.")
    else:
        cur.execute('UPDATE apicalltime SET time = ? WHERE apiname = ?', (now, apiname))
        con.commit()
        print("Updated api call time.")

def getApiCallTime(apiname):
    try:
        query = cur.execute("SELECT * FROM apicalltime WHERE apiname = ?", [apiname])
        time = query.fetchone()['time']
        return time
    except Exception as e:
        print(e)
