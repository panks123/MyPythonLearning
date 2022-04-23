#try-except

print("Enter 1st number\n")
a=input()
print("Enter 2nd number\n")
b=input()
try:
    print("Sum of two numbers :",(a)+int(b))
except Exception as e:
    print(e)

print("Will always executed")
