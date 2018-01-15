"""
iterator, tuple, list...
"""

from .mymath import MyMath


def fib(n):
    """
    compute n th Fibonacci number
    """
    a, b = 1, 0
    for _ in range(n - 1):
        a, b = a + b, a
    return b


def is_even(n):
    return n % 2 == 0


def sum_even_fibs(n):
    return sum(filter(is_even, map(fib, range(1, n + 1))))


def set_sum_even_fibs(self, n):
    self.num = sum_even_fibs(n)


MyMath.sum_even_fibs = set_sum_even_fibs
