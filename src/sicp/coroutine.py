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
