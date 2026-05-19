from enum import Flag, auto


class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()

class Movie:
    def __init__(self, name, genres: MovieGenres):
        self.name = name
        self.genres = genres

    def __repr__(self):
        return self.name

    def in_genre(self, genre: MovieGenres):
        if genre in self.genres:
            return True
        else:
            return False



# Входные данные 1
# movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)
#
# print(movie)


# Выходные данные 1
# The Lord of the Rings

# Входные данные 2
movie = Movie('The Lord of the Rings', MovieGenres.ACTION | MovieGenres.FANTASY)

print(movie.in_genre(MovieGenres.FANTASY))
print(movie.in_genre(MovieGenres.COMEDY))
print(movie.in_genre(MovieGenres.ACTION | MovieGenres.FANTASY))

# Выходные данные 2
# True
# False
# True