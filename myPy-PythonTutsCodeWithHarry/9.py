# for loop
list1=[1,2,3,4,1,2,3,45]
for i in list1:
    print(i,end=" ")
print()
list2=[["one",1],["two",2],["three",3],["four",4]]
for i,j in list2:
    print(i,"is",j)

dict={"one":1,"two":2,"three":3,"four":4,"five":5}
print()
for i,j in dict.items():
    print(i, "is", j)

#Quiz

list1=["one",1,5,8,"UDP",9,6,18,"JAH",9,12,8,3]

for item in list1:
    if str(item).isnumeric() and item>6:
        print(item,end=" ")
