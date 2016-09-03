# Creating basic class for movies to be included in fresh_tomatoes webpage.
# class name
class Movie:

	# constructor method with parameters
	def __init__(self, movie_title, movie_storyline, movie_poster_link, movie_trailer_url):
		self.title = movie_title                     # Movie's title
		self.storyline = movie_storyline             # Movie's storyle
		self.poster_image_url = movie_poster_link    # Movie's Image URL
		self.trailer_youtube_url = movie_trailer_url # Movie's Youtube URL