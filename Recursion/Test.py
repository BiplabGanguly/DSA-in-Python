def func(i):
    if i == 0:
        return i
    else:
        return func(i-1)
    
print(func(5))