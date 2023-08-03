'''
A phrase is a string of words separated by the space character " ".
The function last_word takes a phrase(string) as an input,
splits the phrase into a list of strings, and then returns the last
word(string).

Example:
phrase = "the last tree to drop an apple"

    || (splitting by " ")
    \/
            
    ["the", "last", "tree", "to", "drop", "an", "apple"]

    || (indexing last element)
    \/
    
    "apple"

NOTE: uncomment the line below the #TODO: comment, and replace
the "(YOUR CODE HERE)" with appropriate python code.

HINT: your code should involve the following variables: n, words
HINT: If a list A has positive length n, the last element is A[n-1]
'''

def get_last_word(phrase):
    #break down phrase(string) into a list of words
    words = phrase.split(" ")
    
    #get number of words
    n = len(words)

    #TODO: UNCOMMENT THE LINE BELOW AND REPLACE (YOUR CODE HERE)
    #last_word = (YOUR CODE HERE)
    return last_word

#ignore this code
def solution(*args):
    return get_last_word(*args)
