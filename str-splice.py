'''
String splicing is the operation of getting a specific range or
substring based on indices.

If s is a string, then to get the substring from index i to j (exclusive),
we write:

            s[i:j]

NOTE: the character of s at index j is NOT included in the value. i,j are also
known as the 'start' and 'stop' indices.

Here is an example string s with indices shown:

        s | h e l l o   t h e r e
    index | 0 1 2 3 4 5 6 7 8 9 10

Slicing examples with s:  (to try in IDLE, omit the '>>>')
>>> s = "hello there"
>>> s[0:5]
'hello'

>>> s[3:8]
'lo th'

>>> s[6:11]
'there'

>>> s[0:1]
'h'

>> s[2:2]
''

NOTE: The same slicing notation also is valid for lists.
NOTE: Be sure to understand why s[2:2] is the empty string ''

Your task is to write a function substr that takes a string s,
and two integer indices i,j, and returns the substring in s
from index i to index j (exclusive).
'''

def substr(s, i, j):
    #TODO: YOUR CODE BELOW (replace None)
    return None

#ignore this code
def solution(*args):
    return substr(*args)
