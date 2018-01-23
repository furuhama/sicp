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
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value
    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, *args)
        return method
    else:
        return value


def make_class(attributes, base_class=None):
    """
    return a new class,
    which is dispatch dictionary
    """
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)
    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls


def init_instance(cls, *args):
    """
    return a new object with type cls,
    initialized with args
    """
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance


"""
Account class
"""


def make_account_class():
    """
    return a Account class,
    which has deposit & withdraw methods.
    """

    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)

    def deposit(self, amount):
        balance_new = self['get']('balance') + amount
        self['set']('balance', balance_new)
        return self['get']('balance')

    def withdraw(self, amount):
        balance = self['get']('balance')
        if amount > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amount)
        return self['get']('balance')

    return make_class({'__init__': __init__,
                       'deposit': deposit,
                       'withdraw': withdraw,
                       # set class variable like this
                       'interest': 0.02})
