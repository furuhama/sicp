"""
basic functions to make instance, class
"""


def make_instance(cls):
    """
    return a new object instance,
    which is a dispatch dictionary.
    """
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_methods(value, instance)

    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_methods(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value
