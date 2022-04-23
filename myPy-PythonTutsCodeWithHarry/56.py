# json module

import json
data='{"var1":"harry","var2":"larry"}'

parsed=json.loads(data) # If you have a JSON string, you can parse it by using the json.loads()--it returns a dictionary
print(data)
print(parsed)
print(type(parsed))
#print(data['var1'])------this will give error

print(parsed['var1'])    # this will not give any error

#json.load() accepts file object, parses the JSON data,
# populates a Python dictionary with the data and returns it back to you

f=open("data.json")

parsed1=json.load(f)
print(type(parsed1))

print(parsed1)

dict={
    "cities":["Ranchi","Patna","delhi"],
    "fruits":("mango","orange"),
    "numbers":(1,2,3,4.5),
    "isTrue":False,
    "IsFalse":True
}
jsonobj=json.dumps(dict)  #json.dumps() function converts a Python object into a json string
print("json string: ",jsonobj)
print(type(jsonobj))

jsonobj=json.dumps(dict,sort_keys=True)
print(jsonobj)

