'''

You are given a "database" of user medical information by a hospital.
The database is a 2D array (an array of arrays).

Each array in the database is called a row. Each row has a name(string),
age(int), and height(float).

The hospital needs your help to complete a function (print_db) that will
print all rows of the database, where each row has the following output:

    Patient "(name)" is (age) years old and is (height) ft tall.

NOTE: print_db is a special function with no return value,
so delete "return None" after you are done.

HINT: Make sure the double quotes around "(name)" are included in the output
for each row.
'''

database = [
    ["Aditya",      43, 5.64],
    ["Bob",         52, 5.36],
    ["Catherine",   19, 6.10],
    ["Dennis",      23, 4.72],
    ["Ethan",       41, 5.23],
    ["Fatima",      84, 5.64],
    ["Gerald",      12, 5.10],
    ["Hunter",       5, 4.1],
]

def print_db():
    for row in database:
        # YOUR CODE HERE
        print(row)
    
    return None

#ignore this code
def solution(*args):
    return print_db(*args)
