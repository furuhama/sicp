"""
mymath is my functions
"""


def add(x, y):
    """
    add returns sum of its two arguments
    """
    return x + y


def mul(x, y):
    """
    mul returns multiply of two arguments
    """
    return x * y


def square(x):
    """
    square returns square of a argument
    """
    return mul(x, x)


def sum_squares(x, y):
    """
    sum_squares returns sum of square of two arguments
    """
    return add(square(x), square(y))
