'''
Your teacher has written a function called func
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
    if (a):
        return b
    else:
        return True


#ignore this code
def solution(*args):
    return func_simple(*args)

