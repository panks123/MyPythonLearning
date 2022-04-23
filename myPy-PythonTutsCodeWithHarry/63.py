# zip() and sorted() functions

# zip()----The purpose of zip() is to map the similar index of multiple
# containers so that they can be used just using as single entity.

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)   # It will return a zip object

# printing resultant values
print("The zipped result is : ", end="")
print(list(mapped))


# sorted()----Sorted() sorts any sequence (list, tuple) and always returns a list with the elements in sorted manner,
# without modifying the original sequence.

x = [2, 8, 1, 4, 6, 3, 7]

print("Sorted List returned :"),
print(sorted(x))

print("\nReverse sort :"),
print(sorted(x, reverse=True))

print("\nOriginal list not modified :"),
print(x)