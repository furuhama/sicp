"""
chapter 5
"""

def range_print():
    # all elements are set to memory when it is constructed
    r = range(10000, 1000000000)
    # just when it is called by index, its value is calculated
    # lazy computation
    print(r[45006230])


class Letters(object):
    def __init__(self):
        self.current = 'a'

    def __next__(self):
        if self.current > 'd':
            raise StopIteration
        result = self.current
        self.current = chr(ord(result)+1)
        return result

    def __iter__(self):
        return self


def counting():
    counts = [1, 2, 3]
    for i in counts:
        print(i)


def count_by_iter():
    counts = [1, 2, 3]
    i = counts.__iter__()
    try:
        while True:
            item = i.__next__()
            print(item)
    except StopIteration:
        pass


def letters_generation():
    def letters_generator():
        current = 'a'
        while current <= 'd':
            yield current
            current = chr(ord(current)+1)

    for letter in letters_generator():
        print(letter)


def generate_all_pairs():
    test_list = [1, 2, 3, 4]
    def all_pairs(s):
        for i1 in s:
            for i2 in s:
                yield (i1, i2)
    print(list(all_pairs(test_list)))


def using_stream():
    # initialize Stream.empty
    Stream.empty = Stream(None, None, True)

    s = Stream(1, lambda: Stream(2+3, lambda: Stream.empty))
    print(s.first)
    print(s.rest.first)
    print(s.rest)
    ints = make_interger_stream()
    print(ints)
    print(ints.first)
    t = make_interger_stream(3)
    print(t)
    m = map_stream(lambda x: x*x, t)
    print(m)
    l = stream_to_list(truncate_stream(m, 5))
    print(l)
    p1 = primes(make_interger_stream(2))
    p1_l = stream_to_list(truncate_stream(p1, 7))
    print(p1_l)


class Stream(object):
    """ A lazily evaluate recursive list. """
    def __init__(self, first, compute_rest, empty=False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        """ Return the rest of the stream, computing it if necessary. """
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

    def __repr__(self):
        if self.empty:
            return '<empty stream>'
        return 'Stream({0}, <compute_rest>)'.format(repr(self.first))


def make_interger_stream(first=1):
    def compute_rest():
        return make_interger_stream(first+1)
    return Stream(first, compute_rest)


def map_stream(fn, s):
    if s.empty:
        return s
    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)


def filter_stream(fn, s):
    if s.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    return compute_rest()


def truncate_stream(s, k):
    if s.empty or k == 0:
        return Stream.empty
    def compute_rest():
        return truncate_stream(s.rest, k-1)
    return Stream(s.first, compute_rest)


def stream_to_list(s):
    r = []
    while not s.empty:
        r.append(s.first)
        s = s.rest
    return r


def primes(pos_stream):
    def not_divible(x):
        return x % pos_stream.first != 0
    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))
    return Stream(pos_stream.first, compute_rest)
