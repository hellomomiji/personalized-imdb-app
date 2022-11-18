from src.db import get_db
from src.message import render_error, success
from flask import session

con = get_db()
cur = con.cursor()

def getUser_id():
    user = cur.execute("SELECT * FROM users WHERE username = ?", [session['user']]).fetchone()
    return user['id']

def getMovie_id(title):
    movie = cur.execute('SELECT * FROM movies WHERE title = ?', [title]).fetchone()
    return movie['id']
    
    
def getWatchList():
    user_id = getUser_id()
    favoMovies = cur.execute('SELECT * FROM favo WHERE user_id = ?', [user_id]).fetchall()
    ids = [movie['favoMovie_id'] for movie in favoMovies]
    print("CurrentWatchList: " + str(ids))
    movieData = []
    for id in ids:
        cur.execute('SELECT * FROM movies WHERE id = ?', [id])
        movieData.append(cur.fetchone())
    return movieData

def addMovie(title):
    user_id = getUser_id()
    movie_id = getMovie_id(title)
    print('User: ' + str(user_id) + ' Movie: ' + str(movie_id))
    
    # Check wheather exists
    try:
        cur.execute('INSERT INTO favo (user_id, favoMovie_id) VALUES (?, ?)', (user_id, movie_id))
        con.commit()      
        print("Succesfully Added")  
    except Exception as e:
        print(e)

    
def removeMovie(title):
    user_id = getUser_id()
    movie_id = getMovie_id(title)
    cur.execute('DELETE FROM favo WHERE user_id = ? AND favoMovie_id = ?', (user_id, movie_id))
    con.commit()
    print("Successfully removed")