"""
implement calculator
"""

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
