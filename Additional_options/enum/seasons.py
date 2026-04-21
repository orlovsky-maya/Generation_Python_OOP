from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, country: str):
        ru = dict(zip(Seasons, ('зима', 'весна', 'лето', 'осень')))
        en = dict(zip(Seasons, ('winter', 'spring', 'summer', 'fall', )))

        if country == "ru":
            return ru.get(self)
        else:
            return en.get(self)




# Входные данные1
print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))

# Выходные данные1

# осень
# fall
