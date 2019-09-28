def convert_fahr_to_cels(deg_fahr):
    return (deg_fahr - 32) * 5 / 9


def convert():
    deg_fahr = float(input("Temperature F? "))
    print("It is {0} degrees Celsius.".format(convert_fahr_to_cels(deg_fahr)))


if __name__ == '__main__':
    convert()