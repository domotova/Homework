def print_two(a,b):
    print("Arguments: {0} and {1}".format(a,b))


if __name__=='__main__':
    print_two()       #invalid
    print_two(4,1)      #valid
    print_two(41)     #invalid
    print_two(a=4,1)  #invalid
    print_two(4,a=1)  #invalid
    print_two(4,1,1)  #invalid
    print_two(b=4,1)  #invalid
    print_two(a=4,b=1)  #valid
    print_two(b=1,a=4)  #valid
    print_two(1,a=1)  #invalid
    print_two(4,1,b=1)#invalid

    print_two(a=2,b=8,7)  # invalid
    print_two(4,b=1)  # valid