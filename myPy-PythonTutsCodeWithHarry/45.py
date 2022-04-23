# oops--- Operator overloading and dunder/magic methods
# dunder methods -- methods starting  and ending with double underscore


class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def __add__(self, other):   #dunder method
        return self.salary+other.salary

    def __truediv__(self, other):
        return  self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"name is:'{self.name}' salary is:{self.salary} role is:'{self.role}'"

harry=Employee("Harry",12000,'Programmer')
larry=Employee("Larry",13000,'Instructor')

print(harry+larry)
print(larry/harry)

'''
Mapping Operators to Functions
This table shows how abstract operations correspond to operator symbols in the Python syntax and the functions in the 
operator module.
 
 link:: https://docs.python.org/3/library/operator.html
'''


print(harry)   #if __str__() is not present then it will call __repr__()
               #if __str__() and __repr__() both are present then it will call __str__()
               #in that case to call repr we have to write:
print(repr(harry))

print(str(harry)) #if __str__() is not present then this will call __repr__()
