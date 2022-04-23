# Python Practice problem 5 (Easy, 10 points)
# Palindromify The List
# You are given a list which contains some numbers. You have to print a list of next palindromes
# only if the number is greater than 10 otherwise you will print that number.
#
# Input:
#
# [1, 6, 87, 43]
#
# Output:
#
# [1, 6, 88, 44]


def isPalindrome(n):
    if  str(n)==str(n)[::-1]:
        return  True
    else:
        return False

def nextPalindrome(n):
    n=n+1
    while(not isPalindrome(n)):
        n=n+1
    return n

if __name__=='__main__':
    n=int(input("Enter size of list"))
    li=[]
    print(f"Enter {n} elements")
    for i in range(n):
        li.append(int(input()))

    # for i in range(n):
    #     if li[i]>10:
    #         li[i]=nextPalindrome(li[i])
    #
    # print(li)
    print([i if i<=10 else nextPalindrome(i) for i in li] )


