def sum(n):
    m=2
    l=1
    k=2
    S = 0
    float(S)
    while k < n+1:
        if k % 2 == 0:
            m = m*2
        else:
            l = l*2
        S = S + k * (m / (3**k) + l / (3**k))
        k=k+1
    return S


if __name__ == '__main__':
    print(sum(10000))


