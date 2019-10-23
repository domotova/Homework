def collatz_len(n):
    k = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        k = k + 1
    return k


def max_collatz_len(n):
    max = 0
    for i in range(n):
        if collatz_len(i) > max:
            max = collatz_len(i)
    return max


if __name__ == '__main__':
    print(collatz_len(13))
    print(max_collatz_len(1000))
