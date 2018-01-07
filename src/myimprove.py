"""
myimprove is my functions
"""

from src import myabstract


def near(x, f, g):
    """
    near returns bool value, whether f(x) & g(x) is near enough or not
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
    """
    return near(guess, myabstract.square, myabstract.successor)
