import media, fresh_tomatoes, tmdb_api

#movies = [toy_story,avatar,book_of_love,fences,eloise,fallen]
movies_as_lsts = six_random_movies()

#Format: Title, Description, Poster, Youtube
movies = []
for movie in movies_as_lsts:
    movies += [media.Movie(movie[0],movie[1],movie[2],movie[3])]

#Open movies web page using fresh_tomatoes python file
fresh_tomatoes.open_movies_page(movies)
print movies