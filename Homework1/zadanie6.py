def get_largest_perimeter(l):
    d = len(l)
    max_perimeter = 0
    for i in range(0, d-2):
        for j in range(i+1, d-1):
            for k in range(j+1, d):
                if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[k] + l[j] > l[i] and l[i] + l[j] + l[k] > max_perimeter:
                    max_perimeter = l[i] + l[j] + l[k]
    if max_perimeter == 0:
        print('No perimeter')
    else:
        print('The largest perimeter = ' + str(max_perimeter))


if __name__ == '__main__':
    List = input("Write list of number")
    L = List.split()
    l = []
    for i in range(0, len(L)):
        l.append(float(L[i]))
    get_largest_perimeter(l)
