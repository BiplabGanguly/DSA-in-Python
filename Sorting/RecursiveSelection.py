def RecursiveSelection(ll, first_index):
    if first_index >= len(ll):
        return
    
    mini_index = first_index
    for i in range(first_index,len(ll)):
        if ll[i] < ll[mini_index]:
            mini_index = i
    ll[first_index],ll[mini_index] = ll[mini_index],ll[first_index]

    RecursiveSelection(ll,first_index+1)


ll = [6,5,4,3,2,1]
RecursiveSelection(ll,0)
print(ll)
