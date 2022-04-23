#excercise 10


import requests
import pickle

# r=requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
# content=r.text
# contents=content.split('\n')
# print(contents)
# contentlist=[]
# for i in contents:
#     contentlist.append(i.split(','))
# print(contentlist)


#pickling

# fileobj=open('contents.pkl','wb')
# pickle.dump(contentlist,fileobj)
# fileobj.close()

#de-pickling

fileobj=open('contents.pkl','rb')
contentlists=pickle.load(fileobj)
print(contentlists)