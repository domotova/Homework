nums = [0, 1, 2, 3]
fruits = ['apple', 'orange', 'pear']
people = ["TA_sam", "student_poohbear", "TA_guido", "student_htiek"]


if __name__ == '__main__':
    print([x * 2 + 1 for x in nums])
    print([s[0].upper() for s in fruits])
    print([s for s in fruits if "p" in s])
    print([letter[3:] for letter in people if "TA" in letter])
    print([(s, len(s)) for s in fruits])
    print({s: len(s) for s in fruits})
