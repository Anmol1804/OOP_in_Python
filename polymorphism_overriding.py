# 4. Method Overriding -> same name, same para

class A:
    def show(self):
        print("in A show")


class B(A):
    
    # this show overrides A show
    def show(self):
        print("in B show")

a1 = B()
a1.show()