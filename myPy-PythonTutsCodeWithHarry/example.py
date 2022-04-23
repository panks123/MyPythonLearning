def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input())
li=[int(x) for x in input().split()]

li1=[]
li2=[]
for i in range(len(li)):
    if(isPrime(li[i])):
        li1.append(li[i])
    else:
        li2.append(li[i])

for i in li1:
    print(i,end=" ")
print()
for i in range(len(li2)-1,-1,-1):
    print(li2[i]," ")


