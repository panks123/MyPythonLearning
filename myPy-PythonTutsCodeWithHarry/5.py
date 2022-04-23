#lists(mutable) and tuples(immutable)

countries=["India","Australia","US","England","Germany"]

numbers=[1,7,4,2,5,9]

mixed=["gdsdg",3,8,6.9,"90"] # lists can have different data type elements

#list slicing and and indexing(same as in Strings)


print(numbers[5:1:-2])#slicing does not affect original string it just returns a new string

#list functions

print(max(numbers))
print(min(numbers))

#fuctions which changes the actual list

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.append(89)
print(numbers)

numbers.extend([100,200,300])
print(numbers)

numbers.insert(2,89)
print(numbers)

numbers.remove(89)#removes first occurence of trhe element(in case of duplicates)
print(numbers)


numbers.pop()#this removes as well as returns the last element
print(numbers)

print(numbers.pop(2))# this will remove element at index 2

print(numbers.pop())



#Tuples

tp=(1,4,3,5,6,8)
tp1=1,4,3,5,6,8  #we can define tuple without () also ,just comma separated elements
print(tp,tp1)

tpl=(1,2,[1,2,3])
print(type(tpl))

print(tpl) # So yes tuples can have list(mutables) as its element
tpl[2][1]=200
print(tpl) # we cannot modify the tuple element but we can modify the list inside the tuple

tp2=(1)
print(tp2)#tuple without () gets printed in case of tuple with single element
print(type(tp2)) # SO tuples containing single element are actually integers 

#practice is
tup3=(1,)
print(tup3)
print(type(tp2))



#trick to swap two numbers in Python

a=3
b=8
a,b=b,a
print(a,b)






