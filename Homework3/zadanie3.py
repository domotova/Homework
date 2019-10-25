def cyclic_string_generator(filename):
    while True:
        for line in open(filename):
            yield line.strip()


if __name__ == '__main__':
    gen = cyclic_string_generator("file.txt")
    for i, line in enumerate(gen):
        print(line)
        if i > 50:
            break
