'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
while(t):
    n=int(input())
    li=[int(i)for i in input().split()]
    print(li)
    k=int(input())
    while(k):
        x=int(input())
        if x in li:
            print("Yes")
        else:
            print("No")
        k-=1

    t-=1
