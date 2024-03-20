# input = 11
# check the number prime or not
# prime number has 2 factors 1 and itself
# output = true

import math
def checkPrime(n:int):
    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            count += 1
            if n%i != i:
                count += 1
    return count

ll = [2,3,4,5,6,7,8,9,10,11,13]

for data in ll:
    if checkPrime(data) == 2:
        print(data,' prime')
    else:
        print(data,' not a prime')