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
            #Trailer has to be called before calling .info()
            movie = tmdb.Movies(num)
            trailer = movie.videos()['results']
            movie = movie.info()
            title = movie['title']
            movies[title] = {}
            #add trailer URL
            processed_url = youtube+trailer['trailer'][0]['key']
            movies[title]['trailer'] = processed_url
            #add poster path
            movies[title]['poster'] = img_url+movie['poster_path']
            #add description
            movies[title]['description'] = movie['overview']
        except:
            attempt += 1
while len(movies) < 6:
    six_random_movies()
    
print movies