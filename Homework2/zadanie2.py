def get_sorted_squares(nums):
    squares = []
    for x in nums:
        squares.append(int(x)**2)
    return sorted(squares)


if __name__ == '__main__':
    nums = input("nums = ").split()
    print(get_sorted_squares(nums))
