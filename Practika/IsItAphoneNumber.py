import re


def is_phone(num):
    return bool(re.match('\d{3} \d{3}-\d{2}-\d{2}$', num))


if __name__ == '__main__':
    print(is_phone("914 276-95-99 ghj"))
    print(is_phone("914 276-95-99"))
    print(is_phone("914 276-595-99"))
    print(is_phone("914 276 95-99"))
