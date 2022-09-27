# inner class

# outer
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    # inner
    class Laptop:
        def __init__(self):
            self.brand = "Lenovo"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student('Anmol', 891)
s1.show()

# print(s1.lap.brand)
lap1 = Student.Laptop()
lap1.show()

# lap2 = s2.lap
# lap2.show()