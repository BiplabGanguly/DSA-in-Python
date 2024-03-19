# Problem statement
# You are given a number ’n’.
# Find the number of digits of ‘n’ that evenly divide ‘n’.
# Note:
# A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.

def countDigits(n: int):
    count=0
    k = n
    while n > 0:
        rem  = n % 10
        if rem == 0:
            n//=10
            continue
        elif  k % rem == 0:
            count += 1
        n //= 10
    return count
