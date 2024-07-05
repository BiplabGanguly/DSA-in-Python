def RecursiveBubble(ll,last_index):
    if last_index <= 0:
        return 
    for i in range(last_index):
        if ll[i] > ll[i+1]:
            ll[i],ll[i+1] = ll[i+1],ll[i]

    RecursiveBubble(ll,last_index-1)


ll = [6,5,4,3,2,1]
RecursiveBubble(ll,len(ll)-1)
print(ll)

