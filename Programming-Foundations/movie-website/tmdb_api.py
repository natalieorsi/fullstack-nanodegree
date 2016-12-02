# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:02:00 2016

@author: norsi

This code will not run without an API key from The Movie DB!
"""
import tmdbsimple as tmdb
import random
#be sure to download the tmdbsimple lib using pip install tmdbsimple

youtube = 'http://www.youtube.com/watch?v='
img_url = 'http://image.tmdb.org/t/p/w500'


def six_random_movies():
    movies = []
    attempt = 0 #safeguard against infinite loops
    while (len(movies) < 2) and (attempt < 10):
        num = random.randint(1,1000)
        new_movie = []
        try:
            #Trailer has to be called before calling .info()
            movie = tmdb.Movies(num)
            trailer = movie.videos()['results']
            movie = movie.info()
            #add title
            new_movie += [movie['title']]
            #add youtube URL
            processed_url = youtube+trailer['trailer'][0]['key']       
            new_movie += [processed_url]
            #add poster path
            new_movie += [img_url+movie['poster_path']]
            #add description
            new_movie += [movie['overview']]
            print new_movie
        except:
            attempt += 1
            print attempt
        if len(new_movie) == 4:
            movies += [new_movie]
    return movies
result = six_random_movies()
#while result < 6:
 #   six_random_movies()

print result