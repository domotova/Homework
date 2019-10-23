def retry(function):

    def wrapper(*args, **kwargs):
        for i in range(3):
            function(*args, **kwargs)

    return wrapper


@retry
def is_agree():
    valid_answer = ["y", "Y"]
    answer = input("Type 'Y' if you are agree: ")
    if answer in valid_answer:
        print("CONGRATS")
    else:
        print("It's not valid answer")


if __name__ == '__main__':
    is_agree()