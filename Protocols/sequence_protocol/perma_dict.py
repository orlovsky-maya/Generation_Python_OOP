class PermaDict:
    def __init__(self, data=None):
        self.data = data.copy() if data else {}.copy()

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError("Изменение значения по ключу невозможно")
        else:
            self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def keys(self):
        return [i for i in self.data.keys()]

    def values(self):
        return [i for i in self.data.values()]

    def items(self):
        return [(key, value) for key, value in self.data. items()]

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

print(permadict['name'])
print(len(permadict))
# Valid output
# Timur
# 2

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())

# Valid output

# name city age
# name city age
# Timur Moscow 30
# ('name', 'Timur') ('city', 'Moscow') ('age', 30)

permadict = PermaDict()

permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))

# Valid output
# 30
# 1

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)

# Valid output
# 'Изменение значения по ключу невозможно'

d = dict.fromkeys(range(100), None)
attrdict = PermaDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)


# Valid output
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
