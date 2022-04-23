# oops---Abstract base class and abstract method

# abstract class contains abstract methods , it is mandatory for all the sub classes of the abstract classes
# to implement the abstract method of the abstract class otherwise it will give error
# to implement abstract method and abstract class we import as following
# from abc import ABCMeta,abstractmethod      #in pytrhon 3.4 and below  #abstractmethod is a decorator

from abc import ABC,abstractmethod          # above python 3.4


class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0


class Rectangle(Shape):
    type='Rectangle'
    sides=4

    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        return  self.length*self.breadth


class Square(Shape):
    type='Square'
    sides=4

    def __init__(self,l):
        self.length=l

    def area(self):
        return  self.length**2


rect1=Rectangle(30,40)
print(rect1.area())

sq1=Square(5)
print(sq1.area())



# s=Shape()     #we cannot create objects of abstract class
