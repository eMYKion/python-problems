'''
You are given a list of integers A, and an integer t. The goal of the
function (two_sum) is to find two unique indices: i,j such that A[i]+A[j] == t.
This is a well-known problem called TwoSum (sometimes TWOSUM and 2SUM).
A high-level description of the problem is to "find the two numbers in A
that add to t".

One (inefficient) way to solve this problem is called the "Brute Force Method",
where we try all combinations of unique indices i,j and check if
A[i]+A[j] == t. We will implement the brute force method for TwoSum in the
function (two_sum).

We are going to use a 'nested' for-loop, that is, a for-loop inside another
for-loop, example:

=========PYTHON CODE=======
n = 4
for i in range(n):
    for j in range(n):
        print(i,j)
===========================

Try running the above code in another Python file. Note that for EACH
iteration of the outer loop, the inner loop does ALL n of its iterations.
That means the print() function above is called a total of n * n = 16 times.

If we had triple loops:
=========PYTHON CODE=======
n = 4
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k)
===========================
Then, the print statement would be called n * n * n = 64 times. Try running
the above code in a python file.

Finally, once if we find a solution of indices i,j, we will return it as a
length-2 list: [i,j]. If no such i,j exists for which A[i]+A[j] == t, then
we will return an empty list: [].

#HINT: In the #TODO: replace "False" below with an appropriate expression
involving A, i, j and t.
'''

def two_sum(A, t):
    
    n = len(A)
    
    for i in range(n):
        for j in range(n):
            #TODO: replace "False" below with an appropriate expression
            if (i != j and False):
                return [i,j]
    return []

# ignore this code
def solution(A, t):
    sol = two_sum(A, t)
    if sol != []:
        sol = [min(sol), max(sol)]
    return sol
