class AttributesMixin:
    def get_public_attributes(self):
        attributes  = list(self.__dict__.items())
        items = [x for x in attributes if not x[0].startswith("_")]
        return items

    def get_protected_attributes(self):
        attributes  = list(self.__dict__.items())
        items = [x for x in attributes if x[0].startswith("_") and "__" not in x[0]]
        return items

# Входные данные1
class Cat(AttributesMixin):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self._breed = breed


cat = Cat('Кемаль', 6, 'Британский')
print(cat.get_public_attributes())
print(cat.get_protected_attributes())


# Выходные данные1
# [('name', 'Кемаль'), ('age', 6)]
# [('_breed', 'Британский')]

# Входные данные2
class BankAccount(AttributesMixin):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance

bank_account = BankAccount(245980, 1000)
print(bank_account.get_public_attributes())
print(bank_account.get_protected_attributes())
# Выходные данные2
# []
# [('_account_number', 245980)]