def cyclic_string_generator(filename):
    while True:
        for line in open(filename):
            yield line.strip()


if __name__ == '__main__':
    gen = cyclic_string_generator("file.txt")
    filtered_nod = filter(lambda x: "NOD19" in x, gen)
    for i, line in enumerate(filtered_nod):
        print(line)
        if i > 50:
            break

