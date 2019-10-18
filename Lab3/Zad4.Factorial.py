import operator
from functools import reduce


def fact(n):
    return reduce(lambda a, b: operator.mul(a, b), [i for i in range(1, n + 1)], 1)


if __name__ == '__main__':
    print(fact(3))  # => 6
    print(fact(7))  # => 5040