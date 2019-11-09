class Pizza:
    def __init__(self, radius, toppings, slices=8):
        self.__radius = radius
        self.toppings = toppings
        self.slices_max = slices
        self.slices_left = slices

    def eat_slice(self):
        if self.slices_left > 0:
            self.slices_left -= 1
        else:
            print("No Pizza")

    def __repr__(self):
        return '{}" Pizza with {}/{} slices '.format(self.__radius, self.slices_left, self.slices_max)


if __name__ == '__main__':
    my_pizza = Pizza(14, ['tomatos', 'cheeze'], 12)
    print(my_pizza)
    my_pizza.__radius = 10
    print(my_pizza)
