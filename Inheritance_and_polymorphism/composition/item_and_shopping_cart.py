class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.price}$"

class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items

    def add(self, item):
        self.items.append(item)

    def total(self):
        summa = 0
        for item in self.items:
            summa += item.price
        return summa

    def remove(self, name_item: str):
        self.items = list(filter(lambda item: item.name != name_item, self.items))

    def __str__(self):
        return '\n'.join(str(i) for i in self.items)

# Sample Input 1:
#
# item1 = Item('Yoga Mat', 130)
# item2 = Item('Flannel Shirt', 22)
#
# print(item1)
# print(item2)

# Sample Output 1:

# Yoga Mat, 130$
# Flannel Shirt, 22$

# Sample Input 2:

shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())

# Sample Output 2:
#
# Yoga Mat, 130$
# Flannel Shirt, 22$
# 152

#
# shopping_cart = ShoppingCart()
#
# print(shopping_cart)



# TEST_3:
shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())

# TEST_3:
# Flannel Shirt, 22$
# 22