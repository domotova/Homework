import operator
if __name__ == '__main__':
    print(operator.add(1, 2))  # => 3
    print(operator.mul(3, 10))  # => 30
    print(operator.pow(2, 3))  # => 8
    print(operator.itemgetter(1)([1, 2, 3])) # => 2