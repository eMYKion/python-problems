'''
Your challenge is to complete reverse_list, which takes as input
a list (my_list) and outputs another list with the elements from my_list
in reverse order.

Example 1:
my_list = [2, 5, 1, -7]
output = [-7, 1, 5, 2]

NOTE: Slicing is not allowed for this problem.
HINT: You may want to use the .append() and .pop() methods
'''

def reverse_list(my_list):
    reversed_list = []

    #while my_list not empty
    while(len(my_list) > 0):
        #pop last element of my_list
        last = my_list.pop()
        
        #YOUR CODE HERE
    
    return reversed_list

#ignore this code
def solution(*args):
    return reverse_list(*args)
