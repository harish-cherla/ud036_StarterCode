import webbrowser


class Movie():
    """Class for movies data"""
    def __init__(self, movieTitle, movieStory, posterImage, trailerLink):
        """Initialize movies data with Movie class obzect"""
        self.title = movieTitle
        self.story = movieStory
        self.poster_url = posterImage
        self.trailer_url = trailerLink

    def show_trailer(self):
        """Open the Movie object trailer in the default browser"""
        webbrowser.open(self.trailer)
        
#EOF
