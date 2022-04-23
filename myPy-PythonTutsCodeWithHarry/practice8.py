# Rohan Das Is A Fraud:
#
# Rohan das is a fraud by nature.
#
# Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values
# (randomly generated) as wrong.
#
# Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
#
# So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates
# Rohan’s multiplication table.
#
# Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
#
# Note: Rohan’s function returns a list of numbers like this
#
# Rohan Das’s Function Input:
#
# rohanMultiplication(6)
#
# Rohan’s function returns this output:
#
# [6, 12, 18, 26, …., 60]
#
# You have to write a function isCorrect(table, number) and return the index where rohan’s function
# is wrong and printit to the screen! If the table is correct, your function returns None.
from random import  randint

def rohansTable(n):
    ranNum=randint(3,9)
    table=[]
    for i in range(1,11):
        if i==ranNum:
            ran=randint(0,n-1)
            table.append(n*i+ran)

        else:
            table.append(n*i)
    return table

def isCorrect(rohTable,number):

    for i in range(1,11):
        if not rohTable[i-1]  == number*i:
            return i
    return None

if __name__=='__main__':
    n=int(input("Enter the number to get it's table"))
    rohTable=rohansTable(n)
    print(f"Rohan's table: {rohTable}")

    index=isCorrect(rohTable,n)
    if index is not  None:
        print(f"Rohan is a fraud, he has provided incorrect value for {n} X {index} = {rohTable[index-1]}  "
              f" Actual value should be {n*index}")
    else:
        print("Rohan has provided a correct table this time")