# Abstract Classes and Methods

# by default py doesnt support
# we use ABC(Abstract base classes) module


# Methods have only declaration are abstract methods    
# We cant create obj of abstract classes


from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        # print("Running")
        pass

# Laptop class must have process method
class Laptop(Computer):
    def process(self):
        print("laptop running")




# c1 = Computer()
# c1.process()

l1 = Laptop()
l1.process()