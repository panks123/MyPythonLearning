#excercise4


b=bool(int(input("Enter 0/1")))
n=int(input("Enter no. of rows for the pattern:\n\n"))

if(b==True):
    for i in range(1,n+1):
        print(i*"*")
else:
    for i in range(n,0,-1):
        print(i*"*")

