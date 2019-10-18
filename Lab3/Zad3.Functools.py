"""
def lcm(*nums):
    if nums == ():
        return 1
    else:
        a = nums[0]
        for i in range(len(nums) - 1):
            b = nums[i+1]
            m = a * b
            while a != 0 and b != 0:
                if a > b:
                    a %= b
                else:
                    b %= a
            a = m//(a+b)
        return a
"""
from functools import reduce
from math import gcd


def lcm(*nums):
    return reduce(lambda a, b: (a * b) // gcd(a, b), nums, 1)


if __name__ == '__main__':
    print(lcm(3, 5))
    print(lcm(41, 106, 12))
    print(lcm(1, 2, 6, 24, 120, 720))
    print(lcm(3))
    print(lcm())
