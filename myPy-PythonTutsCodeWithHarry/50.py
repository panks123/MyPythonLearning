# comprehensions

li=[]
for i in range(20):
    if i%3==0:
        li.append(i)
print(li)

# the above code can be simply written using list comrehension
# list comprehension

li1=[i for i in range(20) if i%3==0]
print(li)

# here in list comprehension condition(if statement) is optional
li=[i for i in range(20)]
print(li)


# like list comprehension we also have dictionary comprehension

# dictionary comprehension

dict1={i:f"Item {i}" for i in range(1,11)}
print(dict1)

dict2={i:f"Item {i}" for i in range(1,11) if i%2==0}
print(dict2)

dict3={i:li1[i] for i in range(len(li1))}
print(dict3)

# reversing key value pair in dictionary using dictionary comprehension

dict1={value:key for key,value in dict1.items()}
print(dict1)

#set comprehension

dresses={dress for dress in ['dress1','dress2','dress3','dress1','dress2','dress3','dress4']}
print(dresses)


# generator comprehension----for generator comprehension we use parenthesis ()

gen=(i for i in range(20) if i%2==0)
print(type(gen))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
for i in gen:
    print(i)
