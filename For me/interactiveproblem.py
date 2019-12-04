if __name__ == '__main__':
    l1 = 1
    l2 = 1
    r1 = 10
    r2 = 10
    while l1 < r1 or l2 < r2:
        m1 = (l1 + r1) // 2
        s = "?{}{}{}".format(1, 0, m1)
        print(s, flush=True)

        if (input()=='1'):
            r1 = m1
        else:
            l1 = m1+1

        m2 = (l2+r2)//2
        s = "?{}{}{}".format(0, 1, m2)
        print(s, flush=True)

        if (input() == '1'):
            r2 = m2
        else:
            l2 = m2+1
    print("!{}{}".format(r1-1, r2-1), flush=True)
