# setters and property decorators


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
    #now we want that when email gets changed then fname and lname of the Employee object gets changed accordingly

    #for this we write : @attribute.setter

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
amyra_dastur=Employee("Amyra","Dastur")

print(pankaj_kumar.details())
print(pankaj_kumar.email)     #because of the @property decorator

pankaj_kumar.fname='Aditya'
print(pankaj_kumar.email)


pankaj_kumar.email='this_that@email.com'
print(pankaj_kumar.fname)
print(pankaj_kumar.lname) #the attributes has been changed
print(pankaj_kumar.email)


#del pankaj_kumar.email      ----we can't directly delete like this because after this statement it checks for a deleter
del pankaj_kumar.email

print(pankaj_kumar.email)