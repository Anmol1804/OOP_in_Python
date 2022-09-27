# classes and objects

class Computer:

    # Special method for defining attributes
    # Constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Configs are : ", self.cpu, self.ram)



# obj creation
com1 = Computer('i5', 16)
com2 = Computer('amd3', 8)
# print(type(com1))


# Computer.config(com1)
com1.config()
com2.config()


print(com1.ram > com2.ram)

