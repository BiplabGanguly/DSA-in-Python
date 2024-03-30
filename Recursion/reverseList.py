'''
reverse a list [1,2,3,4,5,6] = [6,5,4,3,2,1] 
'''


def reverse_list(nums:list[int], lidx:int , ridx: int):
    if lidx >= ridx:
        return nums
    else:
        nums[lidx], nums[ridx] = nums[ridx], nums[lidx]
        return reverse_list(nums, lidx+1, ridx-1)
    
ll = [1,2,3,4,5,6]
print(reverse_list(ll, 0, len(ll)-1))