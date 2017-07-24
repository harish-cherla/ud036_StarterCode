# Movie-Trailer-Project (ud036_StarterCode)

A simple movie trailer website project for Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube.

## Table of contents

- [Demo](#demo)
- [Download](#download)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Copyright and license](#copyright-and-license)

## Demo

For a demo, check out <http://harish-cherla.github.io/ud036_StarterCode/trailer.html>!

## Download

The files for the project, may be [downloaded here](https://github.com/harish-cherla/ud036_StarterCode/archive/master.zip).

## Quick Start

After downloading the project files, a movie trailer page can be created by importing [media.py](https://github.com/harish-cherla/ud036_StarterCode/blob/master/media.py) and [fresh_tomatoes.py](https://github.com/harish-cherla/ud036_StarterCode/blob/master/fresh_tomatoes.py) at the start of your Python script. Then create idividual Movie objects by calling media.Movie() and supplying it with four arguments -- title, storyline, poster_url, and trailer_url. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an array of the movie objects you created. 

```
import media
import fresh_tomatoes

#information for object arguments
title = "Your movie"
story = "Tour story line"
poster_url = "mage_URL"
trailer_url = "Your youtube link"

# Create Movie object
yourMovie = media.Movie(title, year, poster_url, trailer_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([yourMovie])

```

A more detailed example with multiple movie objects, which is used for the [demo](https://github.com/harish-cherla/ud036_StarterCode/blob/master/trailer.html), can be found in [entertainment_center.py](https://github.com/harish-cherla/ud036_StarterCode/blob/master/entertainment_center.py) 


### What's included

Within the download you'll find the following files:

```
master.zip/
├── entertainment_center.py
├── trailer.html
├── template.tpl
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Documentation

### Movie object class

The Movie object class consists of four class variables, a simple constructor method, and a class method for playing a Movie object's movie trailer. The code is located in [media.py](https://github.com/harish-cherla/ud036_StarterCode/blob/master/media.py). 

##### constructor method

The constructor method is called when a new Movie object is created and must include four arguments -- [title](#movietitle), [story](#moviestory), [poster_url](#movieposter_url), and [trailer_url](#movietrailer_url). Each of these arguments is discussed further below.

```
import media

#information for object arguments
title = "Your movie"
story = "Tour story line"
poster_url = "mage_URL"
trailer_url = "Your youtube link"

# Create Movie object
yourMovie = media.Movie(title, year, poster_url, trailer_url)
```

###### movie.title

movie.title is any string used to identify the movie object.

###### movie.year

movie.story is any string used to say somthing about stary

###### movie.poster_url

movie.poster_url is a string containing a URL linking to an image which will be used to represent the Movie object, such as a movie poster or DVD box cover. The movie trailer page portion of this project displays these images with a width of 188px and a height of 292px. So, images with a ratio of 1:1.5 will work best. 

###### movie.trailer_url

movie.trailer_url is a string containing a URL linking to the movie trailer on YouTube.com. The movie trailer page portion of the this project extracts the YouTube id from the URL, so while links to other video services are valid in the Movie class object, they will not work with the movie trailers page. 

##### show_trailer method

show_trailer can be called on any Movie class object to launch that object's movie trailer in a webpage. This method is useful for testing but is not used by the script that generates the finished movie trailers page.

### Movie Trailer Page Functions 

The functions used to create the final movie trailers page are located in [fresh_tomatoes.py](https://github.com/harish-cherla/ud036_StarterCode/blob/master/fresh_tomatoes.py). This file must be imported to access the functions described below.

#### open_movies_page function

To create the static movie trailers page the open_movies_page function must be called and supplied with one required argument (an array of Movie class objects).And uses the [template.tpl](https://github.com/harish-cherla/ud036_StarterCode/blob/master/template.tpl) to craete the [trailer.html](https://github.com/harish-cherla/ud036_StarterCode/blob/master/trailer.html) . 

```
# Create movie trailer page with array of Movie class objects
fresh_tomatoes.open_movies_page([movie1, movie2, movie3])

``` 

The newly generated page will be placed in the same directory and named trailer.html. 

## Copyright and License

- Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).

- Additional code contributed by [Harishkumar]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
