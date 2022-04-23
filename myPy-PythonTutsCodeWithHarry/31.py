# OOPS 1

# creating first class
class Student:
    pass


# creating instances of class

harry=Student()
larry=Student()

print(harry,larry)

# creating instance variables to the instances

harry.name="Harry"
harry.std=12
harry.section='A'

larry.name='Larry'
larry.section='A'
larry.std=11
larry.subjects=['Physics','Chemistry','Maths']


print(harry.name,harry.section,harry.std,harry)

print(larry.name,larry.section,larry.std,larry.subjects)