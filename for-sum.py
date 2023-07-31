'''
The function add_all is given nums, a list of integers, and returns
the sum of all integers in nums. However, there is one incorrect line in the
code. Can you find the error and fix it?
'''

def add_all(nums):
    # FIX THIS CODE
    total = 0
    for i in nums:
        total *= i
    return total

#ignore this code
def solution(*args):
    return add_all(*args)
