'''
The function max_freq takes as input a string s and outputs the character
that appears the most in the string (the character with the maximum frequency).

If more than one character has the maximum frequency, output any of them.

Example 1:
s = "hello there"
output = "e"
explanation:
"e" appears 3 times
"l" appears 2 times
The rest appears once.

Example 2:
s = "aa bb "
output = "a" (or "b" or " ")
explanation:
All characters appear twice.

The algorithm is to iterate through the string and build a dictionary
that keeps track of how many times each letter appears
(keys are characters, values are integers).

However, there are three missing lines (the #TODO: comments).
Can you fill in these lines?
'''

def max_freq(s):

    #create an empty dictionary
    freq_dict = dict()

    #iterate through each character in s
    for char in s:
        
        if (char in freq_dict):
            #if seen char before, increament char's frequency count
            #TODO: YOUR CODE BELOW
        else:
            #add char to dictionary with value 1
            #TODO: YOUR CODE BELOW

    # find which key had the maxmimum count
    sol = None
    max_count = 0
    for key in freq_dict:
        if max_count < freq_dict[key]:
            max_count = freq_dict[key]
            #TODO: UPDATE sol BELOW
            
    return sol

#ignore this code
def solution(*args):
    return max_freq(*args)
