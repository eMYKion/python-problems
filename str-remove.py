'''
Given two strings s and k, the remove_first function returns a new string,
which is s without the first occurence of the string k if possible (if k
is not a substring of s, return the original s).

Example 1:
s="aba", k="a"
output = "ba"

Example 2:
s="hello, world!!!", k=", world"
output = "hello!!!"

Example 3:
s="there is a monster", k="rabbit"
output = "there is a monster"

As an example, let s="hello, world!!!", k=", world".
remove_first works by finding the location of k in s:

              i = first index of k in s
              |
              V
    0 1 2 3 4 5 6 7 8 9   ...   14
s = h e l l o ,   w o r l d ! ! !

Using the length of k and s, we then use string
slicing (see str-slice.py) to get the portion of
s before k (which is s[0:i]), and the portion of s after
k (which is s[i+len(k):len(s)])

              i = first index of k in s
              |
              V
    0 1 2 3 4 5 6 7 8 9   ...   14
s = h e l l o ,   w o r l d ! ! !
    |_______| |<--------->| |___|
     s[0:i]     len(k)      s[i+len(k):len(s)]

HINT: Fill in the definition of i using s,k and any of the string members:
str.split()
str.join()
str.find()
str.startswith()
str.endswith()
'''

def remove_first(s, k):
    # if k is empty or k is not a substring of s 
    if (k == ""):
        return s
    if (not (k in s)):
        return s

    #TODO: UNCOMMENT THE LINE BELOW
    #i = (YOUR CODE HERE)
    s_before_k = s[0:i]
    s_after_k = s[i+len(k):len(s)]
    
    # return concatenation
    return s_before_k + s_after_k

#ignore this code
def solution(*args):
    return remove_first(*args)
