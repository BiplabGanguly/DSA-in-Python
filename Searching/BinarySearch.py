def binary_search(ll:list, key:int):
    left = 0
    right = len(ll)-1
    count = 0

    while left <= right:
        mid = (left+right) //2
        count += 1
        print(count)
        if ll[mid] == key:
            return mid
        elif ll[mid] > key:
            right = mid-1
        else:
            left = mid+1
    return False

ll = []

for i in range(1,33):
    ll.append(i)
print(ll)
print(binary_search(ll,1))