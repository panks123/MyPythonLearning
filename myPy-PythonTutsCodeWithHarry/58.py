#pickle module---dumps and loads


import pickle


fruits=['aam',"santra","seb","angoor","strawberry"]

pickle_obj=pickle.dumps(fruits)     # dumps function returns a binary object after pickling a python object

unpickle_obj=pickle.loads(pickle_obj)  # loads function returns the python object from the binary object
print(unpickle_obj)