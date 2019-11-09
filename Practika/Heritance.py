import time


class Car:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, new_location):
        self.location = new_location

    def __repr__(self):
        return "Car {} at location {}". format(self.name, self.location)

    def __str__(self):
        return "ASD"


#class Taxi(Car):
 #   def passanger_transfer(self, from_point, to_point):
  #      self.move(from_point)
   #     print("Выходите быстро!")
    #    time.sleep(3)
     #   self.move(to_point)


if __name__ == '__main__':
    car = Car('my_car',(0,0))
    print(repr(car))
    print(car)
    #taxi_cab = Taxi("outDriver", (0, 0))
    #print(taxi_cab)
    #taxi_cab.passanger_transfer((10, 20), (30, 40))
    #print(taxi_cab)
