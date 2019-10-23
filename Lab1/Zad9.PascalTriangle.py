def generate_pascal_row(row):
    if not row:
        return [1]
    else:
        row.append(0)
        row.insert(0, 0)
        return [row[i]+row[i+1] for i in range(len(row)-1)]


if __name__ == '__main__':
    print(generate_pascal_row([1, 2, 1]))  # => [1, 3, 3, 1]
    print(generate_pascal_row([1, 4, 6, 4, 1]))  # => [1, 5, 10, 10, 5, 1]
    print(generate_pascal_row([]))  # => [1]
