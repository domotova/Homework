def is_prime(n):
    from math import sqrt
    k = int(sqrt(n))
    m = 0
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, k+1):
            if n % i == 0:
                m = 1
        if m == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    number = input("This number is prime ? ")
    n = int(number)
    is_prime(n)
