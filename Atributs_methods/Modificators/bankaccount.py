from typing import Type


class BankAccount:
    def __init__(self, balance=0):
         self._balance = balance

    def get_balance(self):
        return self._balance


    def deposit(self, amount):
        self._balance += amount
        return self._balance


    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError ('На счете недостаточно средств')
        else:
            self._balance -= amount

    def transfer(self, account: Type['BankAccount'], amount):
        self.withdraw(amount)
        account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)