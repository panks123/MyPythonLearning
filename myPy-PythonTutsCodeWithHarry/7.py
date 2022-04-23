# sets --- always contain unique elements

s1={1,2,3,4,5}
print(s1)

s2=set()   #creates an empty set
s2.add(1)  # used to add new elements
s2.add(3)
print(s2)

s3=set([1,3,5,7])
print(s3)

# set functions

s3.remove(7) # Used to remove a particular element
print(s3)


print(s1.union({8,6,5}))

print(s1.intersection({4,1,2,8,6,5}))

print(s1.difference(s3))

print(s1.isdisjoint(s2))

print(s1.issubset(s2))

print(s1.issuperset(s2))
