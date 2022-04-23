#writing and appending in a file

f=open("16.txt","w")#If the file is not present it will create a new file
#a=f.write("Pankaj is not a good boy")

a=f.write("Pankaj is a good boy\n")#f.write() returns the no. of characters it has written
print(a)#This will print the number of characters it has written 
f.close()


f=open("16.txt","a")
f.write("Pankaj was a good bou but now , he is not.")
#print(f.read())
f.close()


f=open("16e.txt","r+")
# f.write("Pankaj is not a good boy.......")
# print(f.read())
f.write("Pankaj is NOT a good boy.")
f.write("\nYES")
f.close()

