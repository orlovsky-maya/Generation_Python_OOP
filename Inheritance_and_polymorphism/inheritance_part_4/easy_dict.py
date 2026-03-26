class EasyDict(dict):
    def __getattr__(self, item):
        if item in self.keys():
            return self[item]
        else:
            raise KeyError





# Sample Input 1:

easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(easydict.city)

# Sample Output 1:
#
# Timur
# Moscow
#
# Sample Input 2:

easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

easydict['city'] = 'Dubai'
easydict['age'] = 30
print(easydict.city)
print(easydict.age)

# Sample Output 2:
#
# Dubai
# 30
#
# Sample Input 3:

easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)

# Sample Output 3:
#
# {'name': 'Artur', 'city': 'Almetevsk'}



