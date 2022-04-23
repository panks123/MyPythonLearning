import copy
class Test:
    def __init__(self):
        self.a=100
# shallow copy
t1=Test()
t2=copy.copy(t1)
print(t1.a)
print(t2.a)

t2.a=200
print(t1.a)
print(t2.a)

# Deep copy
t3=Test()
t4=copy.deepcopy(t1)
print(t3.a)
print(t4.a)

t4.a=200
print(t1.a)
print(t2.a)