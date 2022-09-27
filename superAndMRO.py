# Constructor behaviour in inheritance
# super() in inheritance
# Method Resolution Order (MRO)
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class D:

    def __init__(self):
        print("In D init")

    def feature1(self):
        print("Feature 1-D working")

# Left to right
#
class C(A,D):
    def __init__(self):
        super().__init__() # get A only as it goes from L to R
        print("In c init")

    def feat(self):
        super().feature2()


# a1 = B()
# a1.feature1()


a2 = C()
a2.feature1()
a2.feat()