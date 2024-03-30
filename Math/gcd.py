# You are given two integers 'n', and 'm'.
# Calculate 'gcd(n,m)', without using library functions.


def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b= b%a
    if a == 0:
        return b
    return a


dict = {12:18,35:42,1071:462,48:18,20:30}

for key in dict:
    data = gcd(key,dict[key])
    print(f'gcd of {key} and {dict[key]} = {data}')
