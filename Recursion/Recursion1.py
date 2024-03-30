'''
Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.
'''

def print_num(n:int):
    if n == 0:
        return n
    else: 
        print_num(n-1)
        print(n)


print_num(5)