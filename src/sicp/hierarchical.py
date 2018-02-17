"""
Some functions for hierarchical structures.
In python, we use tuple for hierarchical structure.
"""

def count_leaves(tree):
    if not isinstance(tree, tuple) :
        return 1
    return sum(map(count_leaves, tree))
