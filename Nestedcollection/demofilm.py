

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

def get_year(m):
    return m.get("year")

movie_dictionary={}

for m in movies:

    release_year=m.get("year")

    if release_year in movie_dictionary:

        movie_dictionary.get(release_year).append(m.get("title"))

    else:

        movie_dictionary[release_year]=[m.get("title")]

print(movie_dictionary)

oldest_movie_data=min(movies,key=get_year)

oldest_movie_data=[m.get("title") for m in movies if m.get("year")==oldest_movie_data.get("year")]

print(oldest_movie_data)

years=[m.get("year") for  m in movies]
print(years)

year_count={y:years.count(y) for y in years}
print(year_count)

genres_count={g for m in movies for g in m.get("genres")}

print(genres_count)


all_genres=[ g for m in movies for g in m.get("genres")]

genres_count={g:all_genres.count(g) for g in all_genres}

print(genres_count)

sorted_movies=sorted(movies,key=lambda mov:mov.get("title")) 

sorted_movies_title=[m.get ("title") for m in sorted_movies]

print(sorted_movies_title)



