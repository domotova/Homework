def cyclic_string_generator(path):
    with open(path) as f:
        k = sum(1 for _ in f)
    while True:
        with open(path) as f:
            for i in range(k):
                new_line = f.readline()
                yield new_line


def len_string_generator(path):
    for line in cyclic_string_generator(path):
        yield sum(map(len, line))-1


if __name__ == '__main__':
    gen = len_string_generator("file.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 50:
            break
