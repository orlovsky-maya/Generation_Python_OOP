class HistoryDict:
    def __init__(self, data=None):
        self.data = data.copy() if data else {}
        self.historical_dict = {key: [value] for key, value in data.items()} if data else {}

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value):
        if key in self.data.keys():
            self.data[key] = value
            self.historical_dict[key].append(value)
        else:
            self.data[key] = value
            self.historical_dict[key] = []
            self.historical_dict[key].append(value)

    def __delitem__(self, key):
        del self.data[key]
        del self.historical_dict[key]

    def keys(self):
        return [i for i in self.data.keys()]

    def values(self):
        return [i for i in self.data.values()]

    def items(self):
        return [(key, value) for key, value in self.data.items()]

    def history(self, key):
        if key not in self.historical_dict:
            return list()
        else:
            return self.historical_dict[key]

    def all_history(self):
        return self.historical_dict

# Test1
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

# Valid output
#
# 99
# 1
# 2

# Test2
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

# Valid output
# ducks cats
# ducks cats
# 99 1
# ('ducks', 99) ('cats', 1)

# Test3
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

# Valid output

# [99, 100]
# [1]
# []

# Test4
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

# Valid output

# {'ducks': [99], 'cats': [1]}
# {'ducks': [99, 100, 101], 'cats': [1, 2]}

# Test5
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))

# Valid output
# 3
# 1

# Test6
historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())

# Valid output
# {'name': ['Irenica'], 'country': ['Russia'], 'level': ['junior']}
# {'name': ['Irenica'], 'country': ['Russia', 'Italy'], 'level': ['junior', 'middle', 'senior']}
# {'name': ['Irenica'], 'country': ['Russia', 'Italy']}
# {'name': ['Irenica'], 'country': ['Russia', 'Italy'], 'level': ['God']}