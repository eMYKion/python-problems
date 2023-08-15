'''
The Fibonacci sequence generates the next item in the sequence by adding the
previous two. The Fibonacci sequence starts with 0 and 1.

Ex.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Note that we can index these numbers, as if they were an "infinite-length"
list:

(fib)    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
(index)  0  1  2  3  4  5  6   7   8   9  10  11  ...

Write a function (fib) that takes the index of this "infinite-length"
sequence, and returns the fibonacci number of that index.

Example 1:
i = 4
output = 3

Example 2:
i = 11
output = 89

Example 3:
i = 7
output = 13
'''

def fib(i):
    # base case
    if i == 0 or i == 1:
        return i

    #recursive case
    #TODO: YOUR CODE BELOW
    return None

# ignore this code
def solution(*args):
    return fib(*args)
