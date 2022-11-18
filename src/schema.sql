DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS favo;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    image TEXT NOT NULL DEFAULT 'https://picsum.photos/200/300',
    releaseYear TEXT DEFAULT 'N/A',
    releaseDate TEXT DEFAULT 'N/A',
    runtime TEXT DEFAULT 'N/A',
    rating TEXT NOT NULL DEFAULT "N/A",
    genres TEXT DEFAULT 'N/A',
    directors TEXT NOT NULL DEFAULT 'N/A',
    stars TEXT NOT NULL DEFAULT "N/A",
    plot TEXT DEFAULT 'N/A',
    intheaters INTEGER NOT NULL DEFAULT 0 CHECK(intheaters IN (0, 1))
);

CREATE TABLE favo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    favoMovie_id INTEGER UNIQUE,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(favoMovie_id) REFERENCES movies(id)

);

CREATE TABLE apicalltime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    apiname TEXT NOT NULL,
    time TEXT NOT NULL DEFAULT 'N/A'
);