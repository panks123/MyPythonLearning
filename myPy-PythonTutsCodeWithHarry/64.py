import copy
# copy.copy ----shallow copy
# copy.deepcopy--- deepcopy

# shallow copy
li1=[[1,2,3],[4,5,6],[7,8,9]]
li2=copy.copy(li1)
# li2[0]=['a','b','c']
# print(id(li1))
# print(id(li2))
# print("li1: ",li1)
# print("li2: ",li2)

li2[0][1]='c'
print(id(li1))
print(id(li2))
print("li1: ",li1)
print("li2: ",li2)

# deep copy

li1=[[1,2,3],[4,5,6],[7,8,9]]
li2=copy.deepcopy(li1)
li2[0][1]='c'
print(id(li1))
print(id(li2))
print("li1: ",li1)
print("li2: ",li2)
