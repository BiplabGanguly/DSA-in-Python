from itertools import combinations

ll = [1,2,3,4,5]
for i,j,k in combinations(ll,3):
    print(i,j,k)