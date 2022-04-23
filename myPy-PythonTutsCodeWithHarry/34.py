# OOps3---Constructors

class Employee:
    no_of_leaves=7   # class variable

    def __init__(self,n,s,r):     # constructor
        self.name=n   # instance variables
        self.sal=s    # instance variables
        self.role=r   # instance variables

    def printdetaails(self):                  # here   self represents the current object
        return f"Name is: {self.name} Salary is: {self.sal} Role is:{self.role}"


harry=Employee("Harry",12000,"Instructor")
larry=Employee("Larry",13000,"Teacher")

print(harry.printdetaails())
print(larry.printdetaails())
