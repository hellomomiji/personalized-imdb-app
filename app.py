from datetime import datetime
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from src.message import render_error, success
from src.MoiveData import getMoviesInTheatersFromAPI, getMoviesInTheatersFromLocal
from src.db import get_db


app = Flask(__name__)

# Configure session to use filesystem
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db = get_db()
cur = db.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ensure username was submitted
        if not request.form.get('username'):
            return render_error('Username required.')
        
        #query for username
        username = request.form.get('username') 
        password = request.form.get('password')
        rows = cur.execute('SELECT * FROM users WHERE username = ?', [username]).fetchone() 
        print(rows)
        if rows and check_password_hash(rows['password'], password):
        # set session of the input username
            session['user'] = username
            print(session['user'])
            return redirect('/')
        
        # error handling
        else:
            return render_error("Not a valid user name or password.")
    else:
        return render_template('login.html')
    
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # check if username is unique
        query = cur.execute('SELECT * FROM users WHERE username = ?', [username]).fetchone()
        if username and password and query is None:
            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                             (username, generate_password_hash(password))
                             )
            db.commit()
            return success("Please go back to login.")
        elif query:
            return render_error('This username already exists.')
        else:
            return render_error("Please try again.")
    else:
        return render_template('register.html')
        

@app.route('/')
def index():
    if 'user' in session and session['user']:
        now = datetime.now().strftime('%A, %d %b %Y %l:%M %p')
        welcomeMessage = "Welcome, " + session['user']
        return render_template('index.html', welcomeMessage=welcomeMessage, now=now)
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    print(session['user'])
    session.clear()
    return redirect('/')


@app.route("/intheaters", methods = ['GET','POST'])
def intheaters():
    if request.method == 'GET':
        movies = getMoviesInTheatersFromLocal()
        print("Movie data retrived from local.")
    else:
        movies = getMoviesInTheatersFromAPI()
        print("API Called. Movie data retrived from API.")
    return render_template('intheaters.html', movies=movies, number=len(movies))

@app.route("/search")
def function2():
    return render_template('search.html')

@app.route("/mywatchlist")
def mywatchlist():
    return render_template('mywatchlist.html')

@app.route("/message", methods=["GET", "POST"])
def error():
    if request.method == "GET": 
        return render_template('message.html')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    