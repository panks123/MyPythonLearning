#Strings(Immutable)

mystr="Pankaj is not a good boy"

#slicing
print(mystr[1:5])
print(mystr[:5])
print(mystr[5:])
print(mystr[:44378])
print(mystr[:])
print(mystr[0:len(mystr):1])
print(mystr[0:len(mystr):2])
print(mystr[0:len(mystr):8821])
print(mystr[::])

# negative slicing
print("Negative slicing: ")
print(mystr[-6:-1])
print(mystr[-1:-(len(mystr)+1):-1])
print(mystr[-1::-1])
print(mystr[:-(len(mystr)+1):-1])
print(mystr[::-1])
print(mystr[-1:-(len(mystr)+1):-3])


# String functions
print("String Functions",end="\n\n\n")

print(mystr.isalnum()) # The isalnum() returns True if all the characters are alphanumeric,meaning alphabet letter (a-z)
                        # and numbers (0-9).
print(mystr.isalpha()) # returns True if all the characters are alphabet letters (a-z).

mystr1="pankajisnotagoodboy"
print(mystr1.isalnum())
print(mystr1.isalpha())

print(mystr.endswith("boy"))
print(mystr.endswith("bdoy"))

print(mystr.startswith("Pankaj"))
print(mystr.startswith("Janj"))

print(mystr.count("o"))

print(mystr1.capitalize())#capitalizes only the starting letter

print(mystr.upper())
mystr2=mystr.upper()
print(mystr2)

print(mystr2.lower())

print(mystr.find("is"))#returns the index of the first occurrence of the string , if not found , returns -1
print(mystr.find("was"))

print(mystr.replace("is","are"))    #replaces first arg with the second one
print(mystr)
mystr3=mystr.replace("is","are")     #so replace function returns a new string after relacing arg1 with arg2
                                     # in the original string but it does not change the original string
print(mystr3)

#for more string functions see python string documentation