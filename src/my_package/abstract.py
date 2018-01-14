"""
abstract is my functions
"""

from .mymath import MyMath


"""
instance methods below
"""


def summation(self, n, term, next_index):
    """
    summation returns sum of any functions
    n: the number of elements for summation
    term: function
    next: how to get next index of element
    """
    total, i = 0, 1
    while i <= n:
        total, i = total + term(i), next_index(i)
    self.num = total


def cube(self, x):
    return x * x * x


def square(self, x):
    return x * x


def identity(self, x):
    return x


def successor(self, x):
    return x + 1


def compose(f, g):
    def h(x):
        return f(g(x))
    return h


def set_composed_value(self, f, g, x):
    composed_function = compose(f, g)
    self.num = composed_function(x)


def sum_cubes(self, n):
    self.summation(n, self.cube, self.successor)


def sum_naturals(self, n):
    self.summation(n, self.identity, self.successor)


def pi_term(self, i):
    """
    pi_term returns 8 / (i * (i + 2))
    """
    return 8 / (i * (i + 2))


def pi_next(self, i):
    """
    pi_next returns i + 4
    """
    return i + 4


def pi_sum(self, n):
    """
    get pi
    """
    self.summation(n, self.pi_term, self.pi_next)


MyMath.summation = summation
MyMath.cube = cube
MyMath.square = square
MyMath.identity = identity
MyMath.successor = successor
MyMath.compose = set_composed_value
MyMath.sum_cubes = sum_cubes
MyMath.sum_naturals = sum_naturals
MyMath.pi_term = pi_term
MyMath.pi_next = pi_next
MyMath.pi_sum = pi_sum
