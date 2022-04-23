# soops---super() and overriding in classes


class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="I am an instance variable in class A"


class B(A):
    #pass
    classvar1 = "I am a class variable in class B"

a=A()
b=B()


print(b.classvar1)       # it will first check for instance variable in the class B ,if not found then it will
                         # check for an instance variabe in its super class B ,if not found then  it will check
                         # for class variable in same class if not found then finally it will check for class
                         # variable in its super class