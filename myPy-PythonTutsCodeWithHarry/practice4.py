# Python Practice problem 4 (Easy, 10 points)
#
# The Next Palindrome
#
# Problem Statement
#
# A palindrome is a string which when reversed is equal to itself:
#
# Examples of palindrome includes 616, mom, 676, 100001
#
# You have to take a number as an input from the user. You have to find the next palindrome corresponding to that
# number. Your first input should be ‘number of test cases’ and then take all the cases as input from the user

# Input:
#
# 3
#
# 451
#
# 10
#
# 2133

# Output:
#
# Next palindrome for 451 is 454
#
# Next palindrome for 10 is 11
#
# Next palindrome for 2133 is 2222


def isPalindrome(n):
    if str(n)==str(n)[::-1]:
        return True

def nextPalindrome(n):
    n=n+1
    while(not isPalindrome(n)):
        n=n+1
    return n


if __name__=='__main__':
    t=int(input("Enter no. of test cases: "))
    numbers=[]
    i=1
    while(t):
        numbers.append(int(input(f"Enter number {i}")))
        i+=1
        t-=1

    for number in numbers:
        print(f"Next palindrome for {number} is: {nextPalindrome(number)}")