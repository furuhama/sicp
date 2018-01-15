"""
function decorators
"""

from .mymath import MyMath


def trace1(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped


# wrap function
@trace1
def triple(x):
    return 3 * x


def set_triple(self, x):
    self.num = triple(x)


MyMath.triple = set_triple
