from abc import ABC, abstractmethod
class Family(ABC):
    def __init__(self, mood="neutral"):
        self.mood = mood

    @abstractmethod
    def greet(self):
        pass

class Father(Family):
    def greet(self):
        return "Hello!"

    def be_strict(self):
        self.mood = "strict"

class Mother(Family):
    def greet(self):
        return "Hi, honey!"

    def be_kind(self):
        self.mood = "kind"

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass




# # Sample Input 1:

father = Father()
mother = Mother()

print(father.mood)
print(mother.mood)
print(father.greet())
print(mother.greet())

# # Sample Output 1:
# #
# # neutral
# # neutral
# # Hello!
# # Hi, honey!
# #
# # Sample Input 2:
#
father = Father('happy')
mother = Mother('unhappy')

print(father.mood)
print(mother.mood)
father.be_strict()
mother.be_kind()
print(father.mood)
print(mother.mood)

# # Sample Output 2:
# #
# # happy
# # unhappy
# # strict
# # kind
# #


# TEST_3:
daughter = Daughter()

print(daughter.greet())
print(daughter.mood)
daughter.be_kind()
print(daughter.mood)
daughter.be_strict()
print(daughter.mood)

# TEST_4:
son = Son()

print(son.greet())
print(son.mood)
son.be_kind()
print(son.mood)
son.be_strict()
print(son.mood)


# # TEST_3:
# Hi, honey!
# neutral
# kind
# strict
#
# # TEST_4:
# Hello!
# neutral
# kind
# strict