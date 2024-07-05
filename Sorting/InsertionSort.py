def insertionSort(ll):
    for i in range(len(ll)):
        temp = ll[i]
        j = i-1
        while ll[i] < ll[j] and j >= 0:
            ll[j+1] = ll[j]
            j -= 1
        ll[j+1] = ll[i]

ll = [10,1,8,4,2]
insertionSort(ll)
print(ll) 