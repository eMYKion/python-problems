'''
Your friend has written an incomplete function called both_even.
Given two lists of positive integers A, B, both_even is supposed to
return True if BOTH A and B contain an even number (False otherwise).

The function is supposed to work according to the following algorithm:
1. See if a has an even number and store the result.
2. See if b has an even number and store the result.
3. Look at the result from 1. and 2., then return True
    if both are true.

However, the function is incomplete. Your job is to complete the code
where it says #TODO: ...

HINT: Below the TODOs, replace "False" with an approrpiate boolean
expression involving x, integer literal(s), comparative operation(s),
arithmetic operations(s), (as you see fit).
'''

def both_even(a, b):

    a_has_even = False
    b_has_even = False
    
    #see if a has an even number
    for x in a:
        #TODO: REPLACE False BELOW WITH YOUR BOOLEAN EXPRESSION
        if (False):
            a_has_even = True

    #see if b has an even number
    #NOTE: the x below is not the same as the x above
    for x in b:
        #TODO: REPLACE False BELOW WITH ANOTHER BOOLEAN EXPRESSION
        if (False):
            b_has_even = True

    # return True iff a and b have even numbers
    return a_has_even & b_has_even

#ignore this code
def solution(*args):
    return both_even(*args)
