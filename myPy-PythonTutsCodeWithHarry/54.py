# os module

import os

print(dir(os))

print(os.getcwd())   # returns the current working directory

f=open("Hamad_ex.txt")   # It checks for the file in current working directory if it is found then
                         # it opens the file otherwise throws error
f.close()


os.chdir("C://")  # Changes the current working
#f=open("Hamad_ex.txt")   #this will give error as we have changed the current working directory and this directory
                         # does not have such file
#f.close()
print(os.getcwd())

os.chdir("D:\myPy-PythonTutsCodeWithHarry")

print("List of files and folders: ",os.listdir())    #returns the list of files and folders present in the current directory

#os.mkdir("NewDirectory")   #this will create a new directory named "NewDirectory"

#os.makedirs("NewDirectory1/NewSubDirectory")  #This will create a new directory 'NewDirectory' and inside this
                                              # it will create a sub directory 'NewSubDirectory' if these directories
                                              # are not already present otherwise it will give error

#os.rename("video.py","video123.py")   #this renames the file name from 'video.py' to 'video123.py'


print("Environment Path: ",os.environ.get("PATH"))   #it return the set environment variables

print(os.path.exists("C://")) #returns True if such path exists
print(os.path.exists("C://abc"))   #otherwise returns False
print(os.path.exists("C://Program files"))

print(os.path.isdir("C://abc"))   #returns True if such directory exists  otherwise returns False
print(os.path.isdir("C://Program files"))

print(os.path.isfile("C://Program files"))
print("file present?:",os.path.isfile( "C://Program Files/Git/usr/etc/profile.d/gawk.csh"))

os.chdir("D:\myPy-PythonTutsCodeWithHarry")
print(os.path.isfile("D:\myPy-PythonTutsCodeWithHarry/51.py"))
file=os.path.splitext("51.py")   #this function splits the file name and extension and returns a tuple
                                 # in which first element is name of file and second element is its extension
print(file)
print(type(file))
print(file[0])
print(file[1])




