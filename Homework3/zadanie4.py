def cyclic_string_generator(filename):
    while True:
        for line in open(filename):
            yield line.strip()


def len_string_generator(path):
    for line in cyclic_string_generator(path):
        yield sum(map(len, line))-1


if __name__ == '__main__':
    gen = len_string_generator("file.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 50:
            break
