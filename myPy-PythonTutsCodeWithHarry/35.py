# oops4---class methods

class Employee:
    no_of_leaves=7   # class variable

    def __init__(self,n,s,r):     # constructor
        self.name=n   # instance variables
        self.sal=s    # instance variables
        self.role=r   # instance variables

    def printdetaails(self):                  # here   self represents the current object
        return f"Name is: {self.name} Salary is: {self.sal} Role is:{self.role}"

    @classmethod
    def change_leaves(cls,leaves):      # here cls refers to  class of the current object
        cls.no_of_leaves=leaves

harry=Employee("Harry",12000,"Instructor")
larry=Employee("Larry",13000,"Teacher")

print(harry.printdetaails())
print(larry.printdetaails())

harry.change_leaves(23)  #earlier we were unable to change the class variable using object but now using
                         # class method we can change the value of the class variable using objects
print(Employee.no_of_leaves)

larry.change_leaves(34)
print(Employee.no_of_leaves)

Employee.change_leaves(12)
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
print(larry.no_of_leaves)
