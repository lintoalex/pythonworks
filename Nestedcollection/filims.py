
movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

# q1 total number of movie

movies_count=len(movies)
# print("movie count",movies_count)

# q2 movies with genere drama

movies_generes=[m.get("title") for m in movies if "Drama" in  m.get("genres")]

# print(movies_generes)

# q3 latest movie

def get_year(mov):

    return mov.get("year")

latest_movie_data=max(movies,key=get_year)

latest_movie=[m.get("title")for m in movies if m.get("year")==latest_movie_data.get("year")]

# print(latest_movie)

# q4 top movie (movie with higest rating)

def get_rating(mov):

    return mov.get("rating")

top_movie_data=max(movies,key=get_rating)

top_rating_movies=[m.get("title") for m in movies if m.get("rating")==top_movie_data.get("rating")]

# print(top_rating_movies)

# q5 movie with languge malayalam

malayalam_movie=[m.get ("title")for m in movies if m.get("language")==("Malayalam")]

# print(malayalam_movie)

# q6 movies released after year 2016

movie_relased=[m.get("title") for m in movies if m.get("year") > 2016]

print(movie_relased)

# q7 movie with lowest rating

# q8 malayalam movies with genre action

# q9 movie released in same year

# q10 oldest movie

# q11 movie name with generes either drama or comedy