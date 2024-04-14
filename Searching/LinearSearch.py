def linear_search(ll:list,key:int):
    for i in ll:
        if i == key:
            return True
    return False


ll = [1,2,3,4,5,6]
print(linear_search(ll,12))