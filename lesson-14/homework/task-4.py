# 4. Task: Movie Recommendation System
#    1. Use this url http://www.omdbapi.com/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random
import json


def movie_finder(genre):
    url = "http://www.omdbapi.com/"
    params = {
        "apikey": "b5d420a5",
        "s": genre,
        "type": "movie"
    }
    response = requests.get(url,params=params)
    data = response.json()

    random_movie = random.choice(data['Search'])
    imdblink = 'https://www.imdb.com/title/'
    print()
    print(f'Movie: {random_movie['Title']}')
    print(f'{imdblink+random_movie['imdbID']}')
    print(f'Type: {random_movie['Type']}')
    print(f'Year: {random_movie['Year']}')


genre = input('Please Type a genre (action, drama, western..): ').strip().lower()
movie_finder(genre)





# jsonn= json.dumps(data,indent=2)
# print(jsonn)




