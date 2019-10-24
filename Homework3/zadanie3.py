def cyclic_string_generator(path):
    with open(path) as f:
        k = sum(1 for _ in f)

    while True:
        with open(path) as f:
            for i in range(k):
                new_line = f.readline()
                yield new_line


if __name__ == '__main__':
    gen = cyclic_string_generator("file.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 50:
            break