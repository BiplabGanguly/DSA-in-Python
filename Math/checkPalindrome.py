# Problem statement
# Check whether a given number ’n’ is a palindrome number.
# Note :
# Palindrome numbers are the numbers that don't change when reversed.
# You don’t need to print anything. Just implement the given function.

def checkPalindrome(num):
    checknum = num
    newnum = 0
    while num > 0:
        rem = num % 10
        newnum = newnum * 10 + rem
        num //=10
    if checknum == newnum:
            return 'palindrome'
    else:
            return 'not palindrome'
        
n=int(input())
print(checkPalindrome(n)) 