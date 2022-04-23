# oops3-- class methods


class Employee:
    no_of_leaves=7   # class variable


    def printdetaails(self):                  # here   self represents the current object
        return f"Name is: {self.name} Salary is: {self.sal} Role is:{self.role}"


harry=Employee()
larry=Employee()

harry.name="Harry"  # instance variable of harry
larry.name="larry"  # instance variable of larry
harry.sal=12000     # instance variable of harry
larry.sal=13000     # instance variable of larry
harry.role='Instructor'   # instance variable of harry
larry.role='Teacher'

print(harry.printdetaails())  # Although we have not passed eny argument but one argument is passed by default with
                              # the function call which is the object for which function has been called
print(larry.printdetaails())

