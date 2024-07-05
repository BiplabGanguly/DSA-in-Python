def sort(ll):
    p = 1
    while p < len(ll):
        k = p
        while k > 0:
            if ll[k] < ll[k-1]:
                ll[k],ll[k-1] = ll[k-1],ll[k]
            k -= 1
        p += 1

ll = [5,4,3,2,1,54,87,22]
sort(ll)
print(ll) 