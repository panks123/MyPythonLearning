#Functions and docstring

def func1():
    print("Hey man , You are great!!!")

func1()


def func2(a,b):
    '''This functions prints addition of two numbers'''
    print("a+b= ",a+b)

func2(1,2)


def func3(a, b):
    return  a+b


v=func3(1, 4)
print(v)

print(func2.__doc__) #docstring: the first line string inside the function is called its docstring
