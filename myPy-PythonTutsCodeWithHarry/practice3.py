# You visit a restaurant called CodeWithHarry and food items in this restaurant are sorted based on their amount of calories. You have to reverse this list of food items containing their calories.
#
# You have to use following three methods to reverse a list:
#
# • Inbuilt method of python
# • Listname[::-1] slicing trick
# • Swapping first element with last one and second element with second last one and so on….
# Input:
# Take a list as an input from the user.
# [5,4,1]
#
# Output:
# [1,4,5]
# [1,4,5]
# [1,4,5]
# All the three methods give same results!

n=int(input("Enter size of list"))
print(f"Enter {n} elements of the list")
li=[]
for i in range(n):
    li.append(int(input()))
li1 = li.copy()
li1.reverse()

print(li1)

li2=li[::-1]
print(li2)

li3=li.copy()
i=0
j=n-1
while(i<j):
    temp=li3[i]
    li3[i]=li3[j]
    li3[j]=temp
    i+=1
    j-=1
print(li3)

if(li1==li2==li3):
    print("All the three methods give same results!")


