# 2. Operator Overloading

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # here + is overloaded
    # in background a + b => a.__add__(b)
    # here add is overloaded for adding two objs

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student(m1, m2)
        return s3

    
    def __gt__(self, other):
        s = self.m1 + self.m2
        o = other.m1 + other.m2

        return s > o

    
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)

s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


print(s1)