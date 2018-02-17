"""
implement calculator
"""

from operator import mul
from functools import reduce

class Exp(object):
    """ A call expression in Calculator. """
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operands_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operands_strs)

def calc_eval(exp):
    """ Evaluate a Calculator expression. """
    if isinstance(exp, (int, float)):
        return exp
    elif isinstance(exp, Exp):
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)

def calc_apply(operator, args):
    """ Apply the named operator to a list of args. """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom

def read_eval_print_loop():
    """ Run a read-eval-print loop for calculator. """
    #  calc_parse is still undefined

    #  while True:
    #      expression_tree = calc_parse(input('calc> '))
    #      print(calc(expression_tree))
