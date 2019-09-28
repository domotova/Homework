def fizzbuzz(n):
    sum = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum = sum+i
    return sum


if __name__ == '__main__':
    print(fizzbuzz(1001))
