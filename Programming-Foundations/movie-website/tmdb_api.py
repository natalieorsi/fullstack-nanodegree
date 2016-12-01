# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:02:00 2016

@author: norsi
"""
import tmdbsimple as tmdb
import random
#be sure to download the tmdb lib using pip install tmdbsimple

#scifi = "http://www.themoviedb.com/discover/movie?with_genres=878"
#connection = urllib.urlopen(scifi)
#print connection.read()
#connection.close()
#print connection

youtube = 'http://www.youtube.com/watch?v='
img_url = 'http://image.tmdb.org/t/p/w500'
titles = {}
videos = {}
images = {}
movies = {}
attempt = 0 #safeguard against infinite loops
#while (len(movies) < 2) and (attempt < 3):
#    num = random.randint(1,1000)
#    try:
#        movie = tmdb.Movies(num).info()
#        print movie.title
#        print movie.videos
#        movies[movie.title] = [movie.videos]
#    except:
#        attempt += 1
#    print movies
num = 500
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

print movies

def vurl(video_obj):
    print video_obj['key']
#print movie.images()['backdrops']
#movies[movie['id']] = {'Video':movie['video'],'Poster':movie['poster_path']}