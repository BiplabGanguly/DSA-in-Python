def check_high_low(ll:list):
    dist = {}
# add values and their frequencies.......
    for i in ll:
        if i in dist:
            dist[i] += 1
        else:
            dist[i] = 1 


    check_low = 99999
    check_high = -1
    low = 0
    high = 0

# check low value........................
    for i,j in dist.items():
        if check_low > j:
            check_low = j
            low  = i
    
#check high vlaue.........................
    for i,j in dist.items():
        if check_high < j:
            check_high = j
            high = i

    return low,high



ll = [1,1,1,1,2,2,2,3,3,4,4,4,4,4,4]
print(check_high_low(ll))