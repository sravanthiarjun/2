import webbrowser


class Movie():
    """this is the class i can use movie() and all so public it access any where
    ""throught out the program so in that class we have to declare some
    ""attributes like that so it will be dispalyed """

    def __init__(
        i,
        movie_title,
        storyline,
        poster_image,
        trailer_youtube
            ):

            i.title = movie_title
            i.storyline = storyline
            i.poster_image_url = poster_image
            i.trailer_youtube_url = trailer_youtube


def show_trailer(j):
    webbrowswer.open(j.trailer_youtube_url)
