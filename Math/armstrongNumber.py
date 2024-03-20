# You have a number 1634
# check the number palindrome or not.
#check palindrome ... 
# number  = 1634
# power of number of digits
# 1^4 + 6^4 + 3^4 + 4^4 = 1634
# this is a palindrome number

def checkArm(num):
    newnum = 0
    checknum = num

    num2 = num 
    countnum = 0

    while num2 > 0:
        countnum += 1
        num2 //= 10

    while num > 0:
        rem = num % 10
        newnum = newnum + pow(rem,countnum)
        num //= 10
    if newnum == checknum:
        return True
    else:
        return False

if checkArm(93084) == True:
    print('armstrong')
else:
    print('not a armstrong') 



