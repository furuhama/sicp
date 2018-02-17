"""
3.4 Exception
"""

def basic_error():
    raise Exception('An basic error occured')

def try_div_zero():
    try:
        x = 1/0
    except ZeroDivisionError as e:
        print('handling a:', type(e))
        print(e)
        x = 0
    return x

def invert_safe(x):
    try:
        return 1/x
    except ZeroDivisionError as e:
        return str(e)
