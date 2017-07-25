import media
import fresh_tomatoes

"""
Creating media objects with 4 args each:
title (movie's title)
story (Two are three lines of story)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""
thor3 = media.Movie(
    "Thor 3",
    "Thor must face the Hulk in a gladiator\
    match and save his people from the ruthless Hela.",
    "https://i.ytimg.com/vi/v8RgYZAAIzY/hqdefault.jpg",
    "v8RgYZAAIzY")

Transformers = media.Movie(
    "Transformers",
    "Cast: Mark Wahlberg, Josh Duhamel, Anthony Hopkins,\
    Laura Haddock, Isabella Moner, Stanley Tucci, John Turturro",
    "https://i.ytimg.com/vi/v-4rYf0x-F4/hqdefault.jpg",
    "v-4rYf0x-F4")

spiderman = media.Movie(
    "Spider Man",
    "Check out the new Spider-Man: Homecoming trailer\
    starring Robert Downey Jr., Tom Holland, and Marisa Tomei!\
    Be the first to watch.",
    "https://i.ytimg.com/vi/YxKbJrjR9qM/hqdefault.jpg",
    "YxKbJrjR9qM")

babyBos = media.Movie(
    "Baby Bos",
    "Thor must face the Hulk in a gladiator match and\
    save his people from the ruthless Hela.",
    "https://i.ytimg.com/vi/Zh1rw_rKRw0/hqdefault.jpg",
    "Cimp-eTe3MU")

kungfu = media.Movie(
    "Kung Fu Ninja",
    "Ninja guys coms for entertain.",
    "https://i.ytimg.com/vi/6K1zDkKavOI/hqdefault.jpg",
    "6K1zDkKavOI")


#Listing all movies into movies array
movies = [thor3, Transformers, spiderman, babyBos, kungfu]

#Creating the movie web page
fresh_tomatoes.open_movies_page(movies)

#EOF
