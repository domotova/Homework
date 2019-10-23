def is_power_of_two(n):
    k = 0
    if n == 1:
        return True
    else:
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            else:
                k = 1
                return False
        if k == 0:
            return True


if __name__ == '__main__':
    number = input("This number is power of two ? ")
    n = int(number)
    is_power_of_two(n)