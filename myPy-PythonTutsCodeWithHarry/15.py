#File IO basics

'''
Modes to open a file
"r" - open file in read mode---default mode
"w" - open file in write mode
"x" - creates file if file does not exist otherwise operation is failed
"a" - append new contents into the file
"t" - text mode (file is in text format)---default mode
"b" - binary mode (for binary files)
"+" - for both read and write
'''

f=open("15.txt")  # --open() returns a file object which is used to access the file
print(type(f))

content=f.read() # used to read the whole content of a file
print(content)


#At last it is a good practice to close the file to free all the resources associated
f.close()



f=open("15.txt","rt")

content=f.read(7)
print("1. ",content)  #reads 7 characters

content=f.read()#Again when we read ,it starts from the next character where we had finished
print("2. ",content)

f.close()

f=open("15.txt")
content=f.read()#reading the content chracter by character
for i in content:
    print(i,end =" ")


f.close()

f=open("15.txt")
print()
for line in f:    #reding the file cintent line by line
    print(line)

f.close()

f=open("15.txt")


print(f.readline())#reads the 1st line
print(f.readline())#reads the 2nd line


f.close()


f=open("15.txt")

print(f.readlines())#Stores the content of the file in a list
f.close()