# input = 12
# divisors = 1,2,3,4,6,12
# sum = 1+2+3+4+6+12 = 28
# output = 28

import math
def sumOfAllDivisor(n:int):
    sumofnum = 0
    i=1
    while i*i <= n :
        if n%i == 0:
            sumofnum += i
            if n//i != i:
                sumofnum += n//i
        i+=1
    return sumofnum   


print(sumOfAllDivisor(12))
