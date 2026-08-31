from dataclasses import dataclass, field


@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist:str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)


# Входные данные1
print(MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012))

# Выходные данные1
# MusicAlbum(title='Calendar', artist='Motorama')

# Входные данные1
musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)

print(musicalbum1 == musicalbum2)
print(musicalbum1 != musicalbum2)

# Выходные данные2
# True
# False

# Входные данные3
musicalbum = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)

try:
    musicalbum.genre = 'Post-punk, New Wave, Indie Rock'
except:
    print('Error')

# Выходные данные3
# Error