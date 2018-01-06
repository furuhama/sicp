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


def pow(x, n):
    """
    pow returns x^n
    """
    return x ** n


def sum_squares(x, y):
    """
    sum_squares returns sum of square of two arguments
    """
    return add(square(x), square(y))


def sum_naturals(n):
    """
    sum_naturals returns sum of 1 to n
    """
    total, i = 0, 1
    while i <= n:
        total, i = total + i, i + 1
    return total
