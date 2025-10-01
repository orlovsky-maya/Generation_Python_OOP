class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        if item == "attrs_num":
            return len(self.__dict__) + 1
        else:
            raise AttributeError


music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)


music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)