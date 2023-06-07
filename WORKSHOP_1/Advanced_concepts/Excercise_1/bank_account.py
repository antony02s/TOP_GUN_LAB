# Write a Python class called
# BankAccount with methods for depositing, withdrawing,
# and checking the account balance.

class Banck_Account:
    def __init__(self, balance):
        self.balance = balance


    def depositing(self,amount):
        self.balance = self.balance + amount

    def withdrawing(self,amount):
        self.balance = self.balance - amount

    def check_balance(self):
        return self.balance