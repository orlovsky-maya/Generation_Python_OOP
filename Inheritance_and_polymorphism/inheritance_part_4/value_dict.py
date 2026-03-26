class ValueDict(dict):

    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        return None

    def keys_of(self, value):
        result = []
        for k, v in self.items():
            if v == value:
                result.append(k)
        return result


# Sample Input 1:

valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))

# Sample Output 1:

# banana
# banana orange

# Sample Input 2:

countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

valuedict = ValueDict(countries)

print(valuedict.key_of('Moscow'))
print(*valuedict.keys_of('Washington'))
#
# Sample Output 2:
#
# None
#
# Sample Input 3:

valuedict = ValueDict({})

print(valuedict.key_of(12))
print(*valuedict.keys_of(33))

# Sample Output 3:
#
# None

