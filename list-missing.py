'''
You are given a list of n integers from 0 to n-1 (like indices),
except that one integer is missing from the list L. The function (missing)
takes as input L, and returns the missing integer. Note that L need not
be in order

We are going to approach this problem by first creating a boolean list
B of length n, that indicates which integers are in the list.

For example, say n=4, L=[0,3,1],

We will set B = [False, False, False, False] initially and
for each element x we see in L, we will 'mark' it by setting
B[x] = True to indicate that x is in L. Note that this is possible
because L only has elements that are also valid indices for B.

By the time we finish scanning L, B will have all True
elements EXCEPT at the index of B that is missing in L.
To find this element, we just need to scan B until we find
the index with the False element.

Complete the function (missing) below, following the #TODO.
'''

def missing(L):
    n = len(L)+1 # since one int missing, add one to get n
    
    #List multiplication creates a list with n False elements
    B = [False] * n # [False, False, False, ..., False]

    # 'mark' every index in L
    
    for x in L:
        B[x] = True

    # scan B for unmarked index
    unmarked_index = -1 # -1 is just an initial value that will be overwritten
    
    for i in range(n):
        #TODO: YOUR CODE BELOW (replace "pass" below)
        pass
    
    return unmarked_index

# ignore this code
def solution(*args):
    return missing(*args)
