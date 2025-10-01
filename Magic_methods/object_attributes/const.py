class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError("Изменение значения атрибута невозможно")

    def __delattr__(self, attr):
        raise AttributeError("Удаление атрибута невозможно")

videogame = Const(name='Cuphead')

videogame.developer = 'Studio MDHR'
print(videogame.name)
print(videogame.developer)

videogame = Const(name='Disco Elysium')

try:
    videogame.name = 'Half-Life: Alyx'
except AttributeError as e:
    print(e)

videogame = Const(name='The Last of Us')

try:
    del videogame.name
except AttributeError as e:
    print(e)