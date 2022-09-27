# Every Time new obj takes new space
class Computer:
    def __init__(self):
        self.name = "Anmol"
        self.age = 21

    def update(self):
        self.age = 30

    def compare(self, other):
        if(self.age == other.age):
            return True
        else:
            return False

c1 = Computer()
# address of memory
# print(id(c1))

c2 = Computer()
# print(id(c2))

# c1.name = "Sujal"
# c1.age = 22

# print(c1.name)
# c1.update()
# print(c1.age)

print(c1.compare(c2))