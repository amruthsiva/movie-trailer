#!/usr/bin/env python
import webbrowser
import media
import fresh_tomatoes

print("Content-type:text/html \n")

it = media.Movie("intime",
                 "https://bit.ly/2x4JgkO",
                 "https://www.youtube.com/embed/6zB6wZKEObc")

tod = media.Movie("total overdose",
                  "https://bit.ly/2kb2LyV",
                  "https://www.youtube.com/embed/yseqtsTfIl8")

nfs = media.Movie("nfs",
                  "https://bit.ly/2KIYvlz",
                  "https://www.youtube.com/embed/K-5EdHZ0hBs")

rr = media.Movie("road rash",
                 "https://bit.ly/2J0Tojk",
                 "https://www.youtube.com/embed/j-ZYwbJtQ9g")

gow = media.Movie("god of war",
                  "https://bit.ly/2Iya969",
                  "https://www.youtube.com/embed/K0u_kAWLJOA")

lde = media.Movie("last day on earth",
                  "https://bit.ly/2x07vkp",
                  "https://www.youtube.com/embed/mNJMQtmWT14")

movies = [it, tod, nfs, rr, gow, lde]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)
