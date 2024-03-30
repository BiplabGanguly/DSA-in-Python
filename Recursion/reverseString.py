'''
reverse a string "apple" = "elppa"
'''


def reverse_string(ans:str):
    return ans[len(ans)::-1]
    
name = "biplab"
print(reverse_string(name))