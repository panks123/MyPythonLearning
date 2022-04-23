#dictionary:{key:value}
# key used is always immutable and keys are always unique
# value used can be any mutable or immutable and values can be repeated

dict={"one":1,"two":2,"three":3,"four":4,"five":5}
print(dict)

print(dict["three"])

#Adding key-value pairs

dict["six"]=6
dict["seven"]=7
print(dict)

#updating a key-value

dict["three"]=33
print(dict)

#deleting a key-value

del dict["two"]
print(dict)


dict1=dict # here dict1 and dict points to same dictionary
del dict1["one"]
#this will delete even in the original dictionary dict
print(dict)

#That is why copy function is used

dict2=dict.copy()#returns a shallow copy
print(dict2)

del dict2["three"]
print(dict2,"\n",dict)


#functions in dictionary

dict.update({"seven":7})#this is same as adding a new: dict["seven"]=7
print(dict)

print(dict.keys())

print(dict.items())

#for additional functions search on internet

dicts={}
for i in range(6):
    dicts[i]=0
print(dicts)

for i in range(6):
    dicts[i] +=1


print(dicts)



