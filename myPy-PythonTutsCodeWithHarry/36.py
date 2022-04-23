# oops5--- class methods as constructors

class Employee:
    no_of_leaves=7   # class variable

    def __init__(self,n,s,r):     #constructor
        self.name=n   #instance variables
        self.sal=s    #instance variables
        self.role=r   #instance variables

    def printdetaails(self):                  #here   self represents the current object
        return f"Name is: {self.name} Salary is: {self.sal} Role is:{self.role}"

    @classmethod
    def change_leaves(cls,leaves):      #here cls refers to  class of the current object
        cls.no_of_leaves=leaves


    @classmethod
    def from_dash(cls,str):     #used as a alternative constructor
        params=str.split("-")
        return cls(params[0],params[1],params[2])  #this will return the instance of the class

    # we can convert it to a single line

    @classmethod
    def from_comma(cls,str):
        return cls(*str.split(","))    #used the concept of *args

harry=Employee.from_dash("Harry-12000-Instructor")  #So we can pass only single string argument to create an object
print(harry.printdetaails())

larry=Employee.from_comma("Larry,13000,Teacher")
print(larry.printdetaails())   #This concept of using a class method as a constructor alternative is helpful when
                               # we have lots of comma separated or dash separated or ... data and we want to crete
                               # objects from them

