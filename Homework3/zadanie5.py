def cyclic_string_generator(filename):
    while True:
        for line in open(filename):
            yield line.strip()


def filter_generator(filename):
    for line in cyclic_string_generator(filename):
        yield list(filter(lambda str: "NOD19" in str, line))


if __name__ == '__main__':
    gen = filter_generator("file.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 50:
            break

