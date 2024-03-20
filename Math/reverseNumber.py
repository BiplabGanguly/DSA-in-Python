# You have a number 123
# the output will be 321

def reverseNumber(num):
    newNum = 0
    while num > 0:
        rem = num % 10
        newNum = newNum*10 + rem
        num //= 10
    return newNum

print(reverseNumber(123))