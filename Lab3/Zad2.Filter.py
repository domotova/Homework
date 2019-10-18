if __name__ == '__main__':
    some_list = ['12', '-2', '0']
    print(list(filter(lambda x: x >= 0, map(int, some_list))))
    # ['12', '-2', '0'] --> ['12', '0']
    some_list2 = ['hello', 'world']
    print(list(filter(lambda x: x[0] != 'h', some_list2)))
    # ['hello', 'world'] --> ['world']
    some_list3 = ['Stanford', 'Cal', 'UCLA']
    print(list(filter(lambda x: len(x) > 4, some_list3)))
    # ['Stanford', 'Cal', 'UCLA'] --> ['Stanford']
    print(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(20))))
    # range(20) --> [0, 3, 5, 6, 9, 10, 12, 15, 18]