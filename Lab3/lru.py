def lru(function):
    cache = {}

    def wrapper(*args):
        if args in cache.keys():
            return cache[args]
        value = function(*args)
        cache[args] = value
        return value

    return wrapper


@lru
def some_function(a, b):
    return a + b


if __name__ == '__main__':
    print(some_function(1, 3))
    print(some_function(1, 3))
