# oops 2 - Instance variable and class variable

class Employee:
    no_of_leaves=7   # class variable
    pass

harry=Employee()
larry=Employee()

harry.name="Harry"  #instance variable of harry
larry.name="larry"  #instance variable of larry
harry.sal=12000     #instance variable of harry
larry.sal=13000     #instance variable of larry
harry.role='Instructor'   #instance variable of harry
larry.role='Teacher'      #instance variable of larry

print(harry.name,harry.sal)
print(larry.name,larry.sal)
print(harry.__dict__)  # gives a dictionary containing the instance variables of the instance
print(larry.__dict__)
print(harry.no_of_leaves)
print(larry.no_of_leaves)
print(Employee.no_of_leaves)
print(Employee.__dict__)
# we can change the value of the class variable using the class only , if we try to change using an instance of the
# class then a new instance variable of that particular instance will be created
#e.g.

larry.no_of_leaves=9
print(Employee .no_of_leaves) # this will print the original class variable

print(larry.__dict__)        # we can see that a new instance variable is added to the instance

print(harry.no_of_leaves)
print(larry.no_of_leaves)

# So using instance variable we can only access the class variable but we cannot change the class variable




