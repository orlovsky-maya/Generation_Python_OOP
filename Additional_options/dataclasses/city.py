from dataclasses import dataclass

@dataclass
class City:
    name: str
    population: int
    founded: int

# Входные данные1
city = City('Tokyo', 14043239, 1457)

print(city)
print(city.name)
print(city.population)
print(city.founded)

# Выходные данные1
# City(name='Tokyo', population=14043239, founded=1457)
# Tokyo
# 14043239
# 1457

# Входные данные2
city1 = City('Tokyo', 14043239, 1457)
city2 = City('New York', 8467513, 1624)
city3 = City('Tokyo', 14043239, 1457)

print(city1 == city2)
print(city1 != city2)
print(city1 == city3)
print(city1 != city3)

# Выходные данные2
# False
# True
# True
# False

# example not dataclass
class City:
    def __init__(self, name, population, founded):
        self.name = name
        self.population = population
        self.founded = founded

    def __repr__(self):
        return f"City(name='{self.name}', population={self.population}, founded={self.founded})"

    def __eq__(self, other):
        if isinstance(other, City):
            return (self.name, self.population, self.founded) == (other.name, other.population, other.founded)
        return NotImplemented