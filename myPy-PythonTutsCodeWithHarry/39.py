# oops---Single inheritance


class Employee:
    no_of_leaves=7   # class variable

    def __init__(self,n,s,r):     #constructor
        print('Employee constructor called')
        self.name=n   #instance variables
        self.sal=s    #instance variables
        self.role=r   #instance variables

    def printdetails(self):                  #here   self represents the current object
        return f"Name is: {self.name} Salary is: {self.sal} Role is:{self.role}"

    @classmethod
    def change_leaves(cls,leaves):      #here cls refers to  class of the current object
        cls.no_of_leaves=leaves


    @classmethod
    def from_dash(cls,str):
        return cls(*str.split("-"))    #used the concept of *args

    # static methods are used when we don't want to use self or cls i.e. when we don't
    # want to use instance variable or class variable inside the function
    @staticmethod
    def printthis(str):
        print("This is good",str)

class Programmer(Employee):
    no_of_holidays=56
    def __init__(self,n,s,r,langs):
        print('Programmer constructor called')
        self.name = n  # instance variables
        self.sal = s  # instance variables
        self.role = r  # instance variables
        self.languages =langs

    def printprog(self):
        return f"Programmer's name is: {self.name} Salary is:{self.sal} Role is:{self.role} Languages are: {self.languages}"

harry=Employee("Harry",12000,"Instructor")
larry=Employee("Larry",13000,"Teacher")

rohan=Programmer("Rohan",18000,"Programmer",['Python','c++'])

print(rohan.printdetails())
print(rohan.printprog())

print(rohan.no_of_leaves) # So Programmer class inherits all the methods and attributes of the Employee class
print(rohan.no_of_holidays)