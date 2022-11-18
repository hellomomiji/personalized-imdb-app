# get movie information from IMDB API
from datetime import datetime
import requests
import json
from src.db import get_db

# exampleMovie = {
#                 'title': 'Black Adam (2022)', 
#                 'plot': 'Nearly 5,000 years after he was bestowed with the almighty powers of the Egyptian gods--and imprisoned just as quickly--Black Adam is freed from his earthly tomb, ready to unleash his unique form of justice on the modern world.', 
#                 'image': 'https://m.media-amazon.com/images/M/MV5BYzZkOGUwMzMtMTgyNS00YjFlLTg5NzYtZTE3Y2E5YTA5NWIyXkEyXkFqcGdeQXVyMjkwOTAyMDU@._V1_Ratio0.6699_AL_.jpg', 
#                 'releaseDate': '21 Oct 2022', 
#                 'runtime': '125 mins', 
#                 'rating': '7', 
#                 'genres': 'Action, Adventure, Fantasy', 
#                 'directors': 'Jaume Collet-Serra', 
#                 'stars': 'Dwayne Johnson, Aldis Hodge, Pierce Brosnan, Noah Centineo'}

def getMoviesInTheatersFromAPI():
    # Call API
    url = "https://imdb-api.com/en/API/InTheaters/k_26vizq0b" # This is a personal API key, should be masked if open to public!!
    response = requests.request("GET", url)
    movies = response.json()["items"]
    
    # Connect db
    con = get_db()
    cur = con.cursor()
    
    # Update movie not in theathers - retrive last call data
    lastCall = cur.execute('SELECT * FROM movies WHERE intheaters IS 1').fetchall()
    lastCallMovieTitles = [item['title'] for item in lastCall]
    print(lastCallMovieTitles)
    thisCallMovieTitles = set()
    
    # add movie data to db if movie in theater not in db
    for item in movies:
        thisCallMovieTitles.add(item['title'])
        # check wheather already in db
        query = cur.execute('SELECT * FROM movies WHERE title = ?', [item['title']]).fetchone()
        if not query:
            cur.execute('INSERT INTO movies '
                        '(title, plot, image, releaseYear, releaseDate, runtime, rating, genres, directors, stars, intheaters) '
                        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                        (item['title'], item['plot'], item['image'], item['year'], item['releaseState'], item['runtimeStr'], item["imDbRating"],item["genres"], item["directors"],item["stars"], 1))

    print(thisCallMovieTitles)
    # Update movie not in theaters - check titles and update db
    for title in lastCallMovieTitles:
        if title not in thisCallMovieTitles:
            cur.execute('UPDATE movies SET inteaters = 0 WHERE title = ?', [title])
            print(title + 'removed from intheaters page.')
            
    # return movies in theaters
    intheaters = cur.execute('SELECT * FROM movies WHERE intheaters = 1').fetchall()
    con.commit()
    return intheaters

def getMoviesInTheatersFromLocal():
    con = get_db()
    cur = con.cursor()
    intheaters = cur.execute("SELECT * FROM movies WHERE intheaters = 1").fetchall()
    print(len(intheaters))
    return intheaters
    
     
'''
   json file format
   { "items":[
       {"id": "tt15791034",
        "title": "Barbarian",
        "fullTitle": "Barbarian (2022)",
        "year": "2022",
        "releaseState": "09 Sep 2022",
        "image": "https://m.media-amazon.com/images/M/MV5BN2M3Y2NhMGYtYjUxOS00M2UwLTlmMGUtYzY4MzFlNjZkYzY2XkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_Ratio0.6699_AL_.jpg",
        "runtimeMins": "102",
        "runtimeStr": "102 mins",
        "plot": "A woman staying at an Airbnb discovers that the house she has rented is not what it seems.",
        "contentRating": "R",
        "imDbRating": "7.1",
        "imDbRatingCount": "73453",
        "metacriticRating": "78",
        "genres": "Horror, Thriller",
        "genreList": [
                    {
                    "key": "Horror",
                    "value": "Horror"
                    },
                    {
                    "key": "Thriller",
                    "value": "Thriller"
                    }
                    ],
        "directors": "Zach Cregger",
        "directorList": [
                        {
                        "id": "nm1199107",
                        "name": "Zach Cregger"
                        }
                        ],
                        "stars": "Georgina Campbell, Bill Skarsgård, Justin Long, Matthew Patrick Davis",
                        "starList": [
                        {
                        "id": "nm3569284",
                        "name": "Georgina Campbell"
                        },
                        {
                        "id": "nm0803889",
                        "name": "Bill Skarsgård"
                        },
                        {
                        "id": "nm0519043",
                        "name": "Justin Long"
                        },
                        {
                        "id": "nm1830723",
                        "name": "Matthew Patrick Davis"
                        }
                        ]
        }, 
    {}
    ]
         
    "errorMessage": "" }
''' 