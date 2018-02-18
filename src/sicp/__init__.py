"""
sicp directory is for Chapter 3
"""

from .rlist import *
from .hierarchical import *
from .exception import *
from .calculator import *
from .sequence import *
from .coroutine import *

def counting_change(a, kinds=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    if a < 0 or len(kinds) == 0:
        return 0
    d = kinds[0]
    return counting_change(a, kinds[1:]) + counting_change(a - d, kinds)

def normal_exp(base, n):
    if n == 0:
        return 1
    return base * normal_exp(base, n-1)

def iter_exp(base, n):
    result = 1
    for _ in range(n):
        result *= base
    return result

# faster than normal_exp()
def fast_exp(base, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return square(fast_exp(base, n//2))
    return base * fast_exp(base, n-1)

def square(x):
    return x * x
