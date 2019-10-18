def alpha_score(upper_letters):
    return sum(map(lambda l: 1+ord(l)-ord('A'), upper_letters))


def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(lambda x: x.isupper(), word)), reverse=True)
    return words[0:2]


if __name__ == '__main__':
    print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))