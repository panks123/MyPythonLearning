#requests module

import requests

r=requests.get("https://financialmodelingprep.com/")    # get method is used to get into the url and get its content (the html data)
print(r) # prints <Response [200]> ---- means request success
print("___________________________________________________________")
print(r.text)   #this will print the content inside the url
