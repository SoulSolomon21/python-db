import csv

from cs50 import SQL

open("tuesday.db", "w").close()

db = SQL("sqlite:///tuesday.db")

db.execute("""CREATE TABLE movies(
    id INTEGER PRIMARY KEY,
    Title TEXT
    )""")

db.execute("""CREATE TABLE genres(
    movie_id INTEGER,
    genre TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies(id) 
    )""")

with open("gross movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Film"].strip().capitalize()
        db.execute("""INSERT INTO movies(Title) VALUES(?)""", name)

        Genre = row["Genre"]
        genre = Genre.capitalize().strip()
        db.execute("""INSERT INTO genres(movie_id,genre) VALUES((SELECT id FROM movies WHERE Title = ?),?)""", name, genre)



