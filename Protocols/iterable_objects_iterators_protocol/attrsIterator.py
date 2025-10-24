class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj.__dict__
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        length = len(self.obj) + self.ind
        if length == self.ind:
            raise StopIteration
        for atr in self.obj:
            self.ind += 1
            return (atr, self.obj.pop(atr))


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
user.profession = 'singer'
user.height = 160

attrsiterator = AttrsIterator(user)

print(*attrsiterator, sep='\n')

# Valid Output:
# ('name', 'Debbie') ('surname', 'Harry') ('age', 77)

class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)

# Valid Output:
# ('name', 'Debbie')
# ('surname', 'Harry')
# ('age', 77)
# ('profession', 'singer')
# ('height', 160)

class Kemal:
    def __init__(self):
        self.family = 'cats'
        self.breed = 'british'
        self.master = 'Kemal'


kemal = Kemal()
attrs_iterator = AttrsIterator(kemal)

print(next(attrs_iterator))
print(next(attrs_iterator))
print(next(attrs_iterator))

# Valid Output:
# ('family', 'cats')
# ('breed', 'british')
# ('master', 'Kemal')


class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')

# Valid Output:
# Атрибуты закончились