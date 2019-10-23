from math import sqrt


def is_prime(num):
    if num <= 0:
        return False
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime():
    cursor = 0
    while True:
        if is_prime(cursor):
            yield cursor
        cursor += 1


if __name__ == '__main__':
    for prime_number in generate_prime():
        print(prime_number)
        if prime_number > 100:
            break