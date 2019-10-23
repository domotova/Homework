def is_self_dividing(n):
    m = n
    l = 0
    while n > 0:
        k = n % 10
        n = n // 10
        if m % k != 0:
            l = 1
            return False
            break
    if l == 0:
        return True


if __name__ == '__main__':
    number = input("This number is self dividing ? ")
    n = int(number)
    if n < 0:
        n = -n
    is_self_dividing(n)
