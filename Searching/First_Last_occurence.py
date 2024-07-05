'''
arr = [1,1,1,1,1,2,2,2]
find the first and last occurence of 1 (key)
'''

# first occurence..........................
def first_occurence(ll:list, key:int):
    st = 0
    ed = len(ll)-1
    first_occ = -1
    while ed >= st:
        mid = st + (ed-st)//2
        if ll[mid] == key:
            first_occ = mid
            ed = mid - 1

        elif ll[mid] > key:
            ed = mid -1
        else:
            st = mid+1

    return first_occ

# last occurence..........................
def last_occurence(ll:list, key:int):
    st = 0
    ed = len(ll)-1
    last_occ = -1
    while ed >= st:
        mid = st + (ed-st)//2
        if ll[mid] == key:
            last_occ = mid
            st = mid + 1

        elif ll[mid] > key:
            ed = mid -1
        else:
            st = mid+1

    return last_occ



ll = [0,1,1,1,1,1,2,2,3,3,3,3]

print('first occ - ', first_occurence(ll,12))
print('last occ - ', last_occurence(ll,12))

print('total occurence - ',last_occurence(ll,3) - first_occurence(ll,3)+1)