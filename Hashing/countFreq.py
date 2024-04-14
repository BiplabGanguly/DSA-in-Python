def countFreq(ll:list):
    dist ={}

    for i in ll:
        if i in dist:
            dist[i] += 1
        else:
            dist[i] = 1

    return dist


ll = [1,1,1,1,2,2,2,2,3,3,3]

dist2 = countFreq(ll)

for i,j in dist2.items():
    print(i," == ",j)