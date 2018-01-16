"""
every Account instance has its holder & balance
"""


class Account(object):
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
