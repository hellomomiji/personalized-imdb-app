DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS intheathers;
DROP TABLE IF EXISTS favo;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    imageUrl TEXT NOT NULL,
    releaseDate TEXT NOT NULL,
    runtime TEXT NOT NULL,
    rating TEXT NOT NULL,
    genres TEXT NOT NULL,
    directors TEXT NOT NULL,
    stars TEXT NOT NULL,
    intheathers INTEGER NOT NULL DEFAULT 0 CHECK(intheathers IN (0, 1))
);

CREATE TABLE favo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    favoMovie_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(favoMovie_id) REFERENCES movies(id)

);