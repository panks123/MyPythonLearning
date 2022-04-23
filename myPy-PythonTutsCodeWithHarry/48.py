#oops---object introspection

class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{self.fname}_{self.lname}@email.com"

    def details(self):
        return f"Employee is : {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set Please set it using setter"
        return f"{self.fname}_{self.lname}@email.com"
    # now we want that when email gets changed then fname and lname of the Employee object gets changed accordingly

    # for this we write : @attribute.setter

    @email.setter
    def email(self,string):
        print("Setting now...")
        names=string.split("@")[0]
        self.fname=names.split('_')[0]
        self.lname = names.split('_')[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


pankaj_kumar=Employee("Pankaj","Kumar")
print(type(pankaj_kumar))
print(id(pankaj_kumar))
print(id("this is a string"))
print(id("this is a string"))
print(id("that is a string"))
print(dir(pankaj_kumar))

import inspect
print(inspect.getmembers(pankaj_kumar))
