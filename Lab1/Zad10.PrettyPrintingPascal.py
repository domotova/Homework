def generate_pascal_row(row):
    if not row:
        return [1]
    else:
        row.append(0)
        row.insert(0, 0)
        return [row[i]+row[i+1] for i in range(len(row)-1)]


def print_pascal_triangle(n):
    i = 0
    row = []
    my_list = []
    string = ""
    while i < n:
        row = generate_pascal_row(row)
        my_list.append(''.join(map(str, row)))
        i += 1
    for item in my_list:
        string = string + item.center(len(my_list[-1])) + '\n'
    return string


if __name__ == '__main__':
    print(print_pascal_triangle(12))  # => [1, 3, 3, 1]
