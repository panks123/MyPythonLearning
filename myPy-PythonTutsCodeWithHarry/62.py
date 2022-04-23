#differince between is and ==

#is----- reference equality- to check two references refer to same object
#==-----value equality-two values have same value

a=[7,8,9]
b=a
print(a==b)
print(a is b)

#creating a copy of a

c=a[:]
print(c==a)
print(c is a)