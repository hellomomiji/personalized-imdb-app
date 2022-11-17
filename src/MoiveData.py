# get movie information from IMDB API
import requests
import json

exampleMovie = {
                'title': 'Black Adam (2022)', 
                'plot': 'Nearly 5,000 years after he was bestowed with the almighty powers of the Egyptian gods--and imprisoned just as quickly--Black Adam is freed from his earthly tomb, ready to unleash his unique form of justice on the modern world.', 
                'image': 'https://m.media-amazon.com/images/M/MV5BYzZkOGUwMzMtMTgyNS00YjFlLTg5NzYtZTE3Y2E5YTA5NWIyXkEyXkFqcGdeQXVyMjkwOTAyMDU@._V1_Ratio0.6699_AL_.jpg', 
                'releaseDate': '21 Oct 2022', 
                'runtime': '125 mins', 
                'rating': '7', 
                'genres': 'Action, Adventure, Fantasy', 
                'directors': 'Jaume Collet-Serra', 
                'stars': 'Dwayne Johnson, Aldis Hodge, Pierce Brosnan, Noah Centineo'}

movies = []

def getMoviesInTheatersFromAPI():
    url = "https://imdb-api.com/en/API/InTheaters/k_26vizq0b"
    response = requests.request("GET", url)
    jsonData = response.json()["items"]
    for item in jsonData:
        movie = {}   
        movie["title"] = item["fullTitle"] 
        movie["plot"] = item["plot"]
        movie["image"] = item["image"]
        movie["releaseDate"] = item["releaseState"]
        movie["runtime"] = item["runtimeStr"]
        movie["rating"] = item["imDbRating"]
        movie["genres"] = item["genres"]
        movie["directors"] = item["directors"]
        movie["stars"] = item["stars"]
        movies.append(movie)

    return movies

def getMoviesInTheatersFromLocal():
    return movies
    
     
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