# Methods
# 1. Class Methods
# 2. Instance Methods -> Accessors and Mutators
# 3. Static methods

class Student:

    school = "VIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3 

    # Accessor Instance Method
    def get_m1(self):
        return self.m1

    # Mutators Instance Method
    def set_m1(self, val):
        self.m1 = val

    # self when dealing with obj
    # cls when delaing with class
    @classmethod         #decorator
    def getSchool(cls):
        return cls.school


    @staticmethod
    def info():
        print("This is Student class")


s1 = Student(12,13,14)
s2 = Student(15,16,17)

print(s1.avg())
print(Student.getSchool())
Student.info()