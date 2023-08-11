'''
You are given a nonnegative integer (positive or zero) in the form of a
list of single-digit integers N. For example, we can represent the integer
4536 with N=[4, 5, 3, 6]. Note that the ith digit of our number is at index i
of N, and the most significant digit is at index 0 always (least significant
digit at index len(N)-1). The most significant digit will never be 0 (the ONLY
exception is N = [0]).

Complete the function (addone), which returns a new list of single-digit
integers representing the addition of N and 1.

Example 1:
N = [4, 5, 3, 6]
output = [4, 5, 3, 7]
explanation: 4536 + 1 = 4537

Example 2:
N = [0]
output = [1]
explanation: 0 + 1 = 1

Example 3:
N = [9, 9, 9, 9, 9, 9]
output = [1, 0, 0, 0, 0 ,0 ,0]
explanation: 999999 + 1 = 1000000

HINT: You can use a while-loop to iterate backwards over a list
HINT: It REALLY helps to work through an example on paper,
writing down the carry and remainder digits.
'''

def addone(N):
    # "corner case"
    if N == [0]:
        return [1]

    L = []
    #TODO: uncomment and replace the (YOUR CODE HERE) lines
    i = len(N)-1
    carry = 1
    while (i >= 0):
        s = N[i] + carry
        carry = s // 10
        #remainder = (TODO: YOUR CODE HERE)
        L.insert(0, remainder)
        i -= 1
    
    if carry != 0:
        #TODO: (YOUR CODE HERE) (delete pass below)
        pass
    
    return L

# ignore this code
def solution(*args):
    return addone(*args)
