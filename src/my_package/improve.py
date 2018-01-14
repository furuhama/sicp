"""
myimprove is my functions
"""

from .mymath import MyMath


def near(x, f, g):
    """
    near returns bool value, whether f(t) & g(t) is near enough or not
    """
    return approx_eq(f(x), g(x))


def approx_eq(x, y, tolerance=1e-5):
    """
    approx_eq returns bool value,
    whether the difference b/w x & y is smaller than tolerance
    """
    return abs(x - y) < tolerance


def iter_improve(update, test, guess=1):
    """
    iter_improve updates guess while test(guess) is False,
    when test(guess) returns True, iter_improve returns that guess value
    """
    while not test(guess):
        guess = update(guess)
    return guess


def golden_update(guess):
    """
    golden_update returns 1 / guess + 1
    """
    return 1 / guess + 1


def golden_test(guess):
    """
    golden_test returns whether guess^2 & guess+1 is near enough or not
    use lambda functions
    """
    return near(guess, lambda x: x * x, lambda x: x + 1)


def square_root(x):
    def average(a, b):
        return (a + b) / 2

    def square(a):
        return a * a

    def update(guess):
        return average(guess, x / guess)

    def test(guess):
        return approx_eq(square(guess), x)

    return iter_improve(update, test)


def set_iter_result(self, update, test, guess=1):
    self.num = iter_improve(update, test, guess)


def set_square_root(self, x):
    self.num = square_root(x)


MyMath.iter_improve = set_iter_result
MyMath.square_root = set_square_root
