#oops---multiple inheritance -Diamond shape problem



class A:
    def met(self):
        print("Method in class A")

class B(A):
    def met(self):
        print("Method in class B")

class C(A):
    def met(self):
        print("Method in class C")

class D(B,C):               #Because during the execution the order is maintained i.e.
                            # first it will check in class B then it will check in class C ,,solves the problem
                            # in python but in other languages which supports multiple inheritance it is not like that
    pass


d=D()
d.met()