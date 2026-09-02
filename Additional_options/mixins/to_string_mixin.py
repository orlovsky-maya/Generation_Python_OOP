class ToStringMixin:
    def __repr__(self):
        d = (self.__dict__)
        six_elements = dict(list(d.items())[:6])

        def fmt(v):
            return f"'{v}'" if isinstance(v, str) else str(v)

        if len(d) > 6:
            l = [f"'{k}': {fmt(v)}" for k, v in six_elements.items()]
            s = f"{{{', '.join(l)}, ...}}"
            return f"{self.__class__.__name__}({s})"
        else:
            return f"{self.__class__.__name__}({(self.__dict__)})"

#
# Входные данные1
class Empty(ToStringMixin):
    pass

obj = Empty()
print(obj)
# Выходные данные1
# Empty({})

# Входные данные2
class Movie(ToStringMixin):
    def __init__(self, title, director, rating):
        self.title = title
        self._director = director
        self.__rating = rating

movie = Movie('Interstellar', 'Christopher Nolan', 8.7)
print(str(movie))
print(repr(movie))
# Выходные данные2
# Movie({'title': 'Interstellar', '_director': 'Christopher Nolan', '_Movie__rating': 8.7})
# Movie({'title': 'Interstellar', '_director': 'Christopher Nolan', '_Movie__rating': 8.7})

# Входные данные3
class Book(ToStringMixin):
    def __init__(self, title, author, publication_year, genre, pages, language, publisher):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.pages = pages
        self.language = language
        self.publisher = publisher

book = Book('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 310, 'English', 'George Allen & Unwin')
print(book)

# Выходные данные3
# Book({'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'publication_year': 1937, 'genre': 'Fantasy', 'pages': 310, 'language': 'English', ...})