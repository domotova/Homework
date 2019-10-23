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

"""
def prime_with_seven_end_generator():
    prime_gen = generate_prime()
    for prime_num in prime_gen:
        if prime_num % 10 == 7:
            yield prime_num
"""


if __name__ == '__main__':
    asd = generate_prime()
    filtered_prime_nums = filter(lambda x: x % 10 == 7, asd)
    for i, prime_number in enumerate(filtered_prime_nums):
        print(prime_number)
        if i > 100:
            break
