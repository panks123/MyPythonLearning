# oops---Access specifiers
# public --can be accessed anywhere in the program
# protected (starts with underscore ) --can be accessed within the same class or in the sub clases
# private(starts with double underscore) --can be accessed within the same class only

class Employee:
    no_of_leaves=9    # public variable
    _var=10           # protected variable
    __var1=100          # private variable
    def __init__(self,name,sal,role):
        self.name=name
        self.salary=sal
        self.role=role

    def printdetails(self):
        return f"Name is:{self.name} Salary is :{self.salary} Role is:{self.role}"

class Programmer(Employee):
    no_of_holidays=56
    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r

harry=Employee("Harry",12000,"Instructor")

print(harry.no_of_leaves)
print(harry._var)
#print(harry.var1) #This give error
# However we can acccess the private variable as:
print(harry._Employee__var1)  #this is called name mangling

# Accessing using derived class object
larry=Programmer('Larry',100000,'Programmer')
print(larry.no_of_leaves)
print(larry._var)
# print(larry.__var1) --- This gives error
# However we can acccess the private variable as:
print(larry._Employee__var1)  # this is called name mangling


