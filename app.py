from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.get("/")
def index():
    movies = []
    with open('movies.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            movies.append(row)
    
    return render_template("index.html", movies=movies)

@app.get("/movie/<int:movie_id>")
def movie_details(movie_id):
    found_movie = None

    with open('movies.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for movie in csv_reader:
            if int(movie['id']) == movie_id:
                found_movie = movie
                break 

    if found_movie:
        return render_template("movie-details.html", movie=found_movie)

    else:
        return "Movie not found!", 404


if __name__ == "__main__":
    app.run(debug=True)