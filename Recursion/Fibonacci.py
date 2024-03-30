
count = 1
def fibo(n,a=0,b=1):
    global count
    if count >= n:
        return a
    else:
        count+=1
        print(a)
        return fibo(n,b,a+b)
    
print(fibo(9))
