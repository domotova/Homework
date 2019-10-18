if __name__=='__main__':
    some_list = ['12', '-2', '0']
    print(list(map(int, some_list)))
# ['12', '-2', '0'] --> [12, -2, 0]
    some_list2 = ['hello', 'world']
    print(list(map(len, some_list2)))
# ['hello', 'world'] --> [5, 5]
    print(list(map(lambda x: x[::-1], some_list2)))
# ['hello', 'world']` --> ['olleh', 'dlrow']
    print(list(map(lambda x: (x, x**2, x**3), range(2, 6))))
# range(2, 6) --> [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
    print(list(map(lambda x: x[0]*x[1], zip(range(2, 5), range(3, 9, 2)))))
# zip(range(2, 5), range(3, 9, 2)) --> [6, 15, 28]

