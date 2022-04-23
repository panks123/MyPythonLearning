# with block to open file

# f=open("16.txt")
# f.read()

# f.close()

# this is equivalent to

with open("16.txt") as f:           # this will open as well as close the file automatically
    print(f.read())


# after this if we read the file as following then it will read the file again from starting
f=open("16.txt")
print(f.readlines()) # readlines() function returns a list of all the lines in the file
f.close()
