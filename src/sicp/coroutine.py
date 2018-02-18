"""
coroutine in Python
"""


def using_coroutine():
    # `m` does coroutine
    m = match("Hoge")

    m.__next__()

    m.send("the Hoge with eyes of flame")

    m.send("came whiffling through the tulgey wood")

    m.send("and burbled as it came")

    # ends coroutine
    m.close()


    # another coroutine
    text = 'Commending spending is offending to people pending lending!'

    matcher = match('ending')

    matcher.__next__()

    read(text, matcher)


    # printer and filter
    printer = print_consumer()
    printer.__next__()

    matcher = match_filter('pend', printer)
    matcher.__next__()

    read(text, matcher)


    # count letters
    s = sum_dicts()
    s.__next__()

    c = count_letters(s)
    c.__next__()

    read(text, c)


def match(pattern):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                print(s)
    except GeneratorExit:
        print('=== Done ===')


def read(text, next_coroutine):
    for line in text.split():
        next_coroutine.send(line)
    next_coroutine.close()


def match_filter(pattern, next_coroutine):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                next_coroutine.send(s)
    except GeneratorExit:
        next_coroutine.close()


# just print what itertor gives to this function
def print_consumer():
    print('Preparing to print')
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print('=== Done ===')


def count_letters(next_coroutine):
    try:
        while True:
            s = (yield)
            counts = { letter: s.count(letter) for letter in set(s) }
            next_coroutine.send(counts)
    except GeneratorExit:
        next_coroutine.close()


def sum_dicts():
    total = {}
    try:
        while True:
            counts = (yield)
            for letter, count in counts.items():
                # add `counts` letter count & `total` memorized letter count
                total[letter] = count + total.get(letter, 0)
    except GeneratorExit:
        max_letter = max(total.items(), key=lambda t: t[1])[0]
        print('Most frequent letter: ' + max_letter)
