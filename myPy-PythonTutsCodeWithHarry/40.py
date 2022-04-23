#oops---Multiple inheritance

class Employee:
    no_of_leaves=9
    var=10
    var=20
    var1=100
    def __init__(self,name,sal,role):
        self.name=name
        self.salary=sal
        self.role=role

    def printdetails(self):
        return f"Name is:{self.name} Salary is :{self.salary} Role is:{self.role}"


class Player:
    no_of_games=4
    var=20
    var1=200
    def __init__(self,name,sal,game):
        self.name=name
        self.sal=sal
        self.game=game

    def printdetails(self):
        return f"Name is: {self.name} Salary is:{self.sal} Game is: {self.game}"



class CoolProgrammer(Employee,Player):   #Multiple inheritance
    language="C++"
    var=30

    def printlanguage(self):
        return f"Language is :{self.language}"

class CoolProgrammer1(Player,Employee):   # Multiple inheritance
    language="Python"
    var=50

    def printlanguage(self):
        return f"Language is :{self.language}"

karan=CoolProgrammer("Karan",12000,'CoolProgrammer')   # it will go and first try to find the constructor in the
                                                       # same class then it will check in Employee class and then in
                                                       # Player class as according to the order of inheritance
print(karan.printlanguage())
print(karan.printdetails()) #here also both Employee and Player classes had printdetails() function but
                            # printdetails() of Employee class is executed


print(karan.var)        # it will go and first try to find var in the
                        # same class then it will check in Employee class and then in
                        # Player class as according to the order of inheritance

print(karan.var1)       # it will go and first try to find var1 in the
                        # same class then it will check in Employee class and then in
                        # Player class as according to the order of inheritance


harry=CoolProgrammer1('Harry',14000,'Tennis')
print(harry.printdetails())

print(harry.printlanguage())

print(harry.var)
print(harry.var1)


