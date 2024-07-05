'''
An array arr is a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
'''

def peak_element(arr: list):
    st = 0
    ed = len(arr) - 1
    while ed > st:
        mid = st + (ed - st) // 2
        if arr[mid] > arr[mid + 1]:
            ed = mid
        else:
            st = mid + 1
    return st  


ll = [0,2,3,1,0]
print(peak_element(ll))