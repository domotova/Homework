def is_beauty(n):
    m = n
    k = 0
    while n > 0:
        k = k + n % 10
        n = n // 10

    if m % k == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    number = input("This number is beauty ? ")
    n = int(number)
    if n < 0:
        n = -n
    is_beauty(n)
