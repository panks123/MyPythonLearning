# Global varibles and nested functions

x=20

def f():
    #x=10
    #print(x)
    global x #global keyword gives permission to the function to change its value inside Otherwise this would not
             # have been possible to change the value of x inside the function
    x=x+20
    print(x)

f()
print(x)

def fout():
    y=10
    def fin(): #the inner function is the property of the outer function only
        global y  #This does not access the above y instead
                  # This will create a global variable y outside all the function i.e outside fout()
        y=111

    print("Before fin()",y)
    fin()
    print("After fin()", y)
    fin()

fout()
print(y)