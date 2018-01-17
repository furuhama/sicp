"""
every Account instance has its holder & balance
"""


class Account(object):
    interest = 0.02  # class attribute

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

    def status(self):
        print("====== basic info ======\n{}\nholder: {}\nbalance: {}".format(
            self, self.holder, self.balance))


class CheckingAccount(Account):
    interest = 0.1
    withdraw_charge = 0.1

    def withdraw(self, amount):
        return Account.withdraw(self, amount * (1 + self.withdraw_charge))


class SavingAccount(Account):
    deposit_charge = 0.1

    def deposit(self, amount):
        return Account.deposit(self, amount * (1 - self.deposit_charge))


class CampaignAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # From Campaign
