'''
Given a sorted list of integers slist, and an integer x,
we can insert x in slist so that the result is still sorted after
insertion.

One way is to find the smallest element in slist larger than x,
starting from the 0th index. In other words, we keep incrementing an index i
until we find the first element larger than x, after which we insert.

Example 1:      insert here
x = 7             |
                  V
slist = [1, 3, 5, 10, 12, 14]
(index)  0  1  2  3   4    5

output = [1, 3, 5, 7, 10, 12, 14]
================================

Example 2:   insert here
x = 2        |
             V
    slist = [5, 8, 13, 16, 19, 25]
    (index)  0  1   2   3   4   5

output = [2, 5, 8, 13, 16, 19, 25]
================================

Example 3:                   insert here
x = 26                         |
                               V
slist = [5, 8, 13, 16, 19, 25]
(index)  0  1   2   3   4   5 (6)

output = [5, 8, 13, 16, 19, 25, 26]
================================

HINT: Fill-in code according to the TODO comments
HINT: in the first #TODO: replace "None" with an appropriate expression involving x,i, and slist
'''

def insert_sorted(slist, x):

    # find insert position i
    i = 0
    # while i is a valid index and x is too large
    while(i < len(slist) and None): #TODO: replace "None" with an appropriate expression
        i+=1

    # TODO: insert x into slist
    
    # return modified slist
    return slist

# ignore this code
def solution(*args):
    return insert_sorted(*args)
