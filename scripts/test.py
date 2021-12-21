"""There are two main frameworks to run unit tests in Python, pytest and unittest."""

cache = {}
def fib(x):
    global cache
    if x in cache:
        return cache[x]
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        val = fib(x - 1) + fib(x - 2)
        cache[x] = val
        return val

if __name__ == '__main__':
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(6) == 8
    assert fib(40) == 102334155
    print("Tests passed")
