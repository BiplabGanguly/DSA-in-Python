def bubbleSort(ll):
    for i in  range(len(ll)):
        for j in range(len(ll)-i-1):
            if ll[j] > ll[j+1]:
                ll[j],ll[j+1] = ll[j+1],ll[j]

ll =[5,12,11,9,2]
bubbleSort(ll)
print(ll)
