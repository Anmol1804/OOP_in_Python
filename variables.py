# Variables
# milage, com are instance vars
# wheels is car var -> static var

class Car:

    wheels = 4

    def __init__(self):
        self.milage = 10
        self.com = "BMW"


Car.wheels = 5

c1 = Car()
print(c1.com, c1.milage, c1.wheels)
