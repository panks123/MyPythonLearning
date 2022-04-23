# break and continue


i=0
while(True):
    print(i,end=" ")
    i+=1
    if i==20:
        break

i=0
print()
while(True):
    i += 1
    if i==7:
        continue
    print(i, end=" ")
    if i==20:
        break


#Quiz


print()
while True:
    i = int(input("Enter a number: "))
    if i>100:
        print("Congrats!!!")
        break
