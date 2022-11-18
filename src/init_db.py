import sqlite3
import json

# connection
db = sqlite3.connect('database.db')

# create database from script
with open('src/schema.sql') as f:
    db.executescript(f.read())
    
cur = db.cursor()

# set default value into database
f = open('src/movie250.json')
data = json.load(f)
movies = data['items']

cur.executemany('INSERT INTO movies '
                '(title, image, releaseYear, rating, stars, intheaters) '
                'VALUES (:title, :image, :year, :imDbRating, :crew, 0)', 
                movies)

db.commit()
db.close()

print("Successfully reset database.")