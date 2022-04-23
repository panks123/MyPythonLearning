# string formatting and f-strings

me="Pankaj"
from1="Basadih"

a="this is %s from  %s"%(me,from1)
print(a)

a="this is {} from  {}"
b=a.format(me,from1)
print(b)
a="this is {1} from  {0}"
b=a.format(me,from1)
print(b)

#f-strings

b=f"This is {me} from {from1}"
print(b)



