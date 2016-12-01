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

movies = {}
def six_random_movies():
    attempt = 0 #safeguard against infinite loops
    while (len(movies) < 6) and (attempt < 10):
        num = random.randint(1,1000)
        try:
            #Trailer info has to be called before calling .info()
            movie = tmdb.Movies(num)
            movies[num] = {'trailer':movie.videos()['results']}

            processed_url = youtube+movies[num]['trailer'][0]['key']
            movies[num]['trailer'] = processed_url
            #add poster path
            movies[num]['poster'] = img_url+movie.info()['poster_path']
            #add movie title
            movies[num]['title'] = movie.info()['title']
            #add description
            movies[num]['description'] = movie.info()['overview']
        except:
            attempt += 1
while len(movies) < 6:
    six_random_movies()
print movies