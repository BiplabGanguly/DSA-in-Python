def selectionSort(ll):
    for i in range(len(ll)):
        mn = i
        for j in range(i,len(ll)):
            if ll[j] < ll[mn]:
                mn = j
        ll[i],ll[mn] = ll[mn],ll[i]


ll = [5,4,3,2,1,7,154,0]
selectionSort(ll)
print(ll) 