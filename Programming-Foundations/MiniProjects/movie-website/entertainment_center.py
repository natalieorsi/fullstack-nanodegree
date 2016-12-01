import media, fresh_tomatoes

#Initialize the 6 media files

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
						"A marine on an alien planet",
						"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

book_of_love = media.Movie("The Book of Love",
						"Jiao Ye (played by Tang Wei) is a casino hostess in Macau who accompanies customers as they gamble and earns a living from their tips. Her father, who brought her to Macau from mainland China, was an inveterate gambler who has since died, leaving her with a large pile of debts and a gambling habit of her own. Despite this, she is a good-natured girl who balances her money problems with a longing to find some meaning in her life and a boyfriend she has feelings for.",
						"https://upload.wikimedia.org/wikipedia/en/6/6e/Book_of_Love_%282016_film%29_poster.jpeg",
						"https://www.youtube.com/watch?v=UYtL8CXTqAU")
fences = media.Movie("Fences",
						"Set in 1950s Pittsburgh, a former Negro League player, now working as a waste collector, struggles to provide for his family and come to terms with the events of his life.",
						r"https://upload.wikimedia.org/wikipedia/en/0/0d/Fences_%28film%29.png",
						"https://www.youtube.com/watch?v=4IYt8A2vu7Y")
eloise = media.Movie("Eloise",
					"Set in a defunct insane asylum known as Eloise, four friends break into the abandoned institution in hopes of finding a death certificate, which will grant one of them the rights to a sizable inheritance.",
					"https://i0.wp.com/teaser-trailer.com/wp-content/uploads/Eloise-new-poster.jpg",
					"https://www.youtube.com/watch?v=_SX8BOHEOAo")
fallen = media.Movie("Fallen",
					"In this terrible-sounding movie, Lucinda Price (Addison Timlin) is sent to a reform academy under the assumption that she has killed a boy.",
					"https://i0.wp.com/teaser-trailer.com/wp-content/uploads/Fallen-new-poster.jpg",
					"https://www.youtube.com/watch?v=O-MRLGxczj8")

#Open movies web page using fresh_tomatoes python file
movies = [toy_story,avatar,book_of_love,fences,eloise,fallen]
fresh_tomatoes.open_movies_page(movies)