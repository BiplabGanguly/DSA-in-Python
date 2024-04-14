ll = [1,1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,4]
dist = {}

for i in ll:
    if i in dist:
        dist[i] += 1
    else:
        dist[i] = 1

ll1 = []

for i,j in dist.items():
    if j > 3:
        ll1.append(i)

print(ll1)