from itertools import product

'''
Your instructor Mayank has written a function called func
at 2AM with very little sleep. Can you re-write func (func_simple) after
simplifying the boolean expressions?
'''


def func(a, b):
    
    if (a & True):
        return b
    
    elif (b ^ ~b):
        return True
    
    else:
        return a


def func_simple(a, b):
    pass


# ignore checking code below
if __name__ == "__main__":
    #check all input combination
    all_correct = True
    
    for arg in product((True, False), repeat=2):
        ref = func(*arg)
        tst = func_simple(*arg)
        if (ref != tst):
            print("ERROR: failed case a=%s, b=%s\n\tGot %s, expected %s" \
                  % (*arg, tst, ref))
            all_correct = False
    if (all_correct):
        print("PASS: both functions have the same ")
