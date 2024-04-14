'''
You are given an array 'arr' of length 'n' containing integers within the range '1' to 'x'.
Your task is to count the frequency of all elements from 1 to n.
Note:
You do not need to print anything. Return a frequency array as an array in the function 
such that index 0 represents the frequency of 1, index 1 represents the frequency of 2, and so on.

'''

def countFrequency(n: int, m: int, edges):
    ll = []
    dist ={}
    for i in edges:
        if i in dist:
            dist[i] += 1
        else:
            dist[i] = 1
        
    for i in range(1,n+1):
        if i in dist:
            ll.append(dist[i])
        else:
            ll.append(0)
    return ll



ll = [11,14,8,3,12,14,1,7,4,3]
print(countFrequency(10,14,ll))