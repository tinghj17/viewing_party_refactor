import re


class Movie:
    def __init__(self, title, genre, rating, host):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.host = host
    
    def update_rating(self, new_rating):
        self.rating = new_rating
        self.rating

movie = Movie("batman", "superhero", 3, "DC")
# #print(movie.rating)
# movie.update_rating(9)
# print(movie.update_rating(9))
# # print(movie.rating)
