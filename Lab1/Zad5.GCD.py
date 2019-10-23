def gcd(a, b):
    for i in reversed(range(min(a, b)+1)):
        if i == 0:
            print(max(a, b))
        else:
            if a % i == 0 and b % i == 0:
                print(i)
                return i


if __name__ == '__main__':
    gcd(10, 25)
    gcd(14, 15)
    gcd(3, 9)
    gcd(1, 1)
