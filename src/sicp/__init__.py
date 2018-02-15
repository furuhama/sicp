"""
sicp directory is for Chapter 3
"""

def counting_change(a, kinds=(50, 25, 10, 5, 1)):
    if a == 0:
        return 1
    if a < 0 or len(kinds) == 0:
        return 0
    d = kinds[0]
    return counting_change(a, kinds[1:]) + counting_change(a - d, kinds)
