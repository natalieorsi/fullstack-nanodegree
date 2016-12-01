import webbrowser

class Video():
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

class Movie(Video):
	"""This class provides a way to save movie information."""
	VALID_RATINGS = ['G','R','PG','PG-13']
	#Refer to Google Python Style Guide
	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
	# would be the TV Show class