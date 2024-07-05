def binary_search(ll: list, key: int, st: int, ed: int):
    if st <= ed:
        mid = st + (ed - st)//2
        if ll[mid] == key:
            return mid
        elif ll[mid] > key:
            return binary_search(ll, key, st, mid - 1)
        else:
            return binary_search(ll, key, mid + 1, ed)
    else:
        return False

ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(ll)
print(binary_search(ll, 8, 0, n - 1))

