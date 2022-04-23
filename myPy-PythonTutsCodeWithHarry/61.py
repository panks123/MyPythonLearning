# raise keyword---- raising an exception explicitly

a=input("Enter your name")
b=input("How much do you earn")
if(int(b)==0):
    raise ZeroDivisionError("b is zero so stopping the program")
if(a.isnumeric()):
    raise Exception("Numbers are not allowed")   #Message passed here as string will come at last if an exception occurs

print(f"Hello! {a}")


# visit : https://docs.python.org/3/library/exceptions.html for python built in exceptions

i=input("Enter your name")
try:
    print(i)
except Exception as e:

    if i=="pankaj":
        raise  ValueError("pankaj is blocked")
    print("Exception handled")
