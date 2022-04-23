# map, filter and reduce functions

list1=["5","10","11","55"]

list2=list(map(int,list1))  # map function takes a function as first arg and an iterable like list or tuple as 2nd arg,
                            # map function applies the function to all the elements of the the 2nd arg
print(list2)
print(list2[2]+5)

def sq(i):
    return i**2
li1=[1,2,3,4,5,6]
li2=list(map(sq,li1))
print(li2)

fsq=lambda x:x**2
li3=list(map(fsq,li1))
print(li3)
cube=lambda x:x**3
lif=[sq,cube]
for i in range(5):
    value=list(map(lambda x:x(i),lif))
    print(value)


#filter function

li=filter(lambda x:x>3,li1)   #filter function filters the elements of the iterable according to the given
                               # function as 1st arg, it returns an object
print(tuple(li))

# reduce function
from functools import reduce

li=[1,2,3,4,5]
x=reduce(lambda x,y:x+y,li) #reduce function is present in functools module
                            # it will reduce the values of an iterable according to the given function
                            #e.g. here we have used it to reduce the values of list li to sum of all the elements
print(x)

li=["a","b","c","d","e"]
x=reduce(lambda x,y:x+y,li) # e.g. here we have used reduce() to reduce concatenate all the elements of the list li
print(x)




