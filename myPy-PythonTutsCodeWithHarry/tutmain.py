def fun(str):
    print(f"This is a function called in tutmain.py which is called in { str}")

def add(n,m):
    return m+n

print(__name__)  #the value of __main__ is '__main__' if we run the same file where we have written it But If we run a file which has
                 # imported this file then it will print the file name where this line is actually written
if __name__=='__main__':
    print(fun("tutmain.py"))   # This part would have been executed when we would have run the program
    o=10                       # which had imported this file
    print(o)                   # But if __name__=='__main__': has prevented it

