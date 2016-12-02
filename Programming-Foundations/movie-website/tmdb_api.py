# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:02:00 2016

@author: norsi

This code will not run without an API key from The Movie DB!
"""
import tmdbsimple as tmdb
import random
#be sure to download the tmdbsimple lib using pip install tmdbsimple
#tmdb.API_KEY = 'Your API key here'
youtube = 'http://www.youtube.com/watch?v='
img_url = 'http://image.tmdb.org/t/p/w500'


def six_random_movies():
    movies = []
    attempt = 0 #safeguard against infinite loops
    while (len(movies) < 6) and (attempt < 10):
        num = random.randint(1,1000)
        new_movie = []
        try:
            #Trailer has to be called before calling .info()
            movie = tmdb.Movies(num)
            trailer = movie.videos()['results'][0]
            trailer_key = trailer['key']
            trailer_site = trailer['site']
            #some movies don't have trailer urls
            if trailer and trailer_site == 'YouTube':
                processed_url = youtube+trailer_key
                movie = movie.info()
                #add title first
                new_movie += [movie['title']]
                #next add description
                new_movie += [movie['overview']]
                #add poster path
                new_movie += [img_url+movie['poster_path']]
                #lastly, add youtube URL
                new_movie += [processed_url]
                                
        except:
            attempt += 1
        #final check to ensure all information is present
        if len(new_movie) == 4: 
            movies += [new_movie]
    return movies
result = six_random_movies()
#one likely redundant final check to ensure 6 movies have been found
while len(result) < 6:
 result = six_random_movies()