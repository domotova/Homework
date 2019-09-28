def get_digit_sum(n):
    if n < 0:
        n = -n
    k = 0
    while n > 0:
        k = k + n % 10
        n = n // 10
    return k


if __name__ == '__main__':
    number = input("Write the number")
    n = int(number)
    get_digit_sum(n)
