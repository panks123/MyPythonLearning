# More on Functions And Decorators in Python


def func1():
    print("Hello!!!")

func2=func1

del func1
# func1()  ----This will give error as func1 function is already deleted

# But a copy of func1 was already created and stored in func2 using which we can call that

func2()


# Function returning a  function

def funcReturner(num):
    if num==0:
        return print
    if num==1:
        return min


a=funcReturner(0)
print(a)
a("HELLO FRENs")
a=funcReturner(1)
print(a)
print(a(1,3,2,4,5))


# function as an argument

def executor(f):
    f("THis is this")

executor(print)

def executor1(f,list1):
    x=f(list1)
    print(x)

executor1(min,[2,1,3,7,4])


# ---------------------------------------------------------DCORATORS----------------------------------------------------

def decorator(func):
    def noexec():
        print("Executing")
        func()
        print("Executed")
    return  noexec
    
@decorator
def myfunc():
    print("Love is life")

# myfunc=decorator(myfunc) ---- This is same as decorator which is written above as @decorator
                              # before myfunc()  function definition
myfunc()




