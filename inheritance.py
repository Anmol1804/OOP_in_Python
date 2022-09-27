# inheritance

# parent/super class
class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


# child/sub class
# single level inheritance
class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


# multilevel inheritance
class C(B):
    def feature5(self):
        print("Feature 5 working")



# multiple inhertance
class D:
    def feature6(self):
        print("Feature 6 working")

class E(A, D):
    def feature7(self):
        print("Feature 7 working")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()


c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

d1 = D()
d1.feature6()

e1 = E()
e1.feature1()
e1.feature2()
e1.feature6()
e1.feature7()

