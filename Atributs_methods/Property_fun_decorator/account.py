def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9


class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        raise AttributeError('Изменение логина невозможно')


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = hash_function(new_password)


account = Account('timyr-guev', 'lovebeegeek')

print(account.password)
account.password = 'verylovebeegeek'
print(account.password)