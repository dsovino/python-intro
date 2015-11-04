import webbrowser


class Movie(object):
    """ This class is for html movie render in a web browser"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Init Function
    def __init__(self, movie_titulo, movie_storyline, movie_year,
                 movie_director, movie_duration, poster_imagen,
                 trailer_youtube):
        self.title = movie_titulo
        self.storyline = movie_storyline
        self.year = movie_year
        self.director = movie_director
        self.duration = movie_duration
        self.poster_image_url = poster_imagen
        self.trailer_youtube_url = trailer_youtube

    # Displays the trailer url from youtube on a webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
