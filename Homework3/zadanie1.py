def lru_cache(function):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache.keys():
            return cache[args]
        if kwargs.values() in cache.keys():
            return cache[kwargs.values()]
        value = function(*args, **kwargs)
        cache[args] = value
        cache[kwargs.values()] = value
        return value

    return wrapper
