'''
A list of integers A is sorted if every subsequent element
is equal to or larger than the last. That means for every index i
from 0 to n-2 (inclusive), A[i] <= A[i+1].

NOTE: Indexing/subscripting any list L with an index i where i > len(L)-1
will cause an error: "IndexError: list index out of range". Make sure that
BOTH indices i and i+1 are in range by restricting i to be LESS THAN n-1.

We say that the empty list (the list with no elements) and any list of
length 1 is already sorted.

Given a list of integers (nums), complete the function (is_sorted) to
return True if nums is sorted, False otherwise.
'''

def is_sorted(nums):
    n = len(nums)
    if (n <= 1): #any length-0 and length-1 lists are sorted
        return True
    
    #TODO: YOUR CODE BELOW
            
    return None #TODO: replace "None" with something else

# ignore this code
def solution(*args):
    return is_sorted(*args)
