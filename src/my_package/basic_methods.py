"""
basic_methods is my basic functions
"""

from .mymath import MyMath


"""
instance methods definition
"""


def print_num(self):
    print(self.num)


def add(self, x, y):
    self.num = x + y


def mul(self, x, y):
    self.num = x * y


def square(self, x):
    self.num = self.mul(x, x)


def pow(self, x, n):
    self.num = x ** n


def sum_naturals(self, n):
    total, i = 0, 1
    while i <= n:
        total, i = total + i, i + 1
    self.num = total


MyMath.print_num = print_num
MyMath.add = add
MyMath.mul = mul
MyMath.square = square
MyMath.pow = pow
MyMath.sum_naturals = sum_naturals
