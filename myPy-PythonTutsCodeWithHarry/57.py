# pickle module

import pickle           # used to pickle /preserve an object(any python object) inside a file

# fruits=['aam',"santra","seb","angoor","strawberry"]
# file="myfruits.pkl"
# fileobj=open(file,'wb')    # 'wb' for writing into the file in binary mode  #so "myfruits.pkl" is a binary file

# pickle.dump(fruits,fileobj)  #first argument is python obj and second arg is file object in which it is to be
# preserved
# fileobj.close()

# so now that we have pickled the list 'fruits'  now we will obtain that preserved object i.e unpickling

file='myfruits.pkl'
fileobj=open('myfruits.pkl','wb')

myfruits=pickle.load(fileobj)
print(myfruits)
print(type(myfruits))
fileobj.close()
# pickle is not considered a good thing because of security reasons and change in versions of python
