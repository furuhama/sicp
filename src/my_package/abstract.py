"""
abstract is my functions
"""

from .__init__ import MyMath


"""
instance methods below
"""


def class_summation(self, n, term, next_index):
    total, i = 0, 1
    while i <= n:
        total, i = total + term(i), next_index(i)
    self.num = total


def class_cube(self, x):
    return x * x * x


def class_successor(self, x):
    return x + 1


def class_sum_cubes(self, n):
    self.summation(n, self.cube, self.successor)


MyMath.summation = class_summation
MyMath.cube = class_cube
MyMath.successor = class_successor
MyMath.sum_cubes = class_sum_cubes


"""
Normal functions below
"""


def summation(n, term, next_index):
    """
    summation returns sum of any functions
    n: the number of elements for summation
    term: function
    next: how to get next index of element
    """
    total, i = 0, 1
    while i <= n:
        total, i = total + term(i), next_index(i)
    return total


def cube(x):
    """
    cube returns x^3
    """
    return x * x * x


def square(x):
    """
    square returns x^2
    """
    return x * x


def successor(x):
    """
    successor returns x + 1
    """
    return x + 1


def identity(x):
    """
    identity returns x
    """
    return x


def sum_cubes(n):
    """
    sum_cubes returns sum of i^3 (i is from 1 to n)
    """
    return summation(n, cube, successor)


def sum_naturals(n):
    """
    sum_naturals returns sum of i (i is from 1 to n)
    """
    return summation(n, identity, successor)


def pi_term(i):
    """
    pi_term returns 8 / (i * (i + 2))
    """
    return 8 / (i * (i + 2))


def pi_next(i):
    """
    pi_next returns i + 4
    """
    return i + 4


def pi_sum(n):
    """
    get pi from summation of fractions
    """
    return summation(n, pi_term, pi_next)
