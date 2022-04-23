# oops6---static methods

# oops--- class methods as constructors

class Employee:
    no_of_leaves=7   # class variable

    def __init__(self,n,s,r):     #constructor
        self.name=n   #instance variables
        self.sal=s    #instance variables
        self.role=r   #instance variables

    def printdetaails(self):                  #here   self represents the current object
        return f"Name is: {self.name} Salary is: {self.sal} Role is:{self.role}"

    @classmethod
    def change_leaves(cls,leaves):      # here cls refers to  class of the current object
        cls.no_of_leaves=leaves


    @classmethod
    def from_dash(cls,str):
        return cls(*str.split("-"))    # used the concept of *args

    # static methods are used when we don't want to use self or cls i.e. when we don't
    # want to use instance variable or class variable inside the function
    @staticmethod
    def printthis(str):
        print("This is good",str)


harry=Employee.from_dash("Harry-12000-Instructor")  # So we can pass only single string argument to create an object
print(harry.printdetaails())

harry.printthis("thing")


#static method can be accessed using object name as well as  class name

Employee.printthis("thing for health")
