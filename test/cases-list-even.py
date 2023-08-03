'''
pairs = [
    ([],[1,2,3]),
    ([],[]),
    ([1,3],[]),
    ([1,3,2],[54]),
    ([1,3,7,],[]),
    ([2,4,6], [8,10,12]),
]
'''

cases = {
    0: (([],[1,2,3]), False),
    1: (([],[]), False),
    2: (([1,3],[]), False),
    3: (([1,3,2],[54]), True),
    4: (([1,3,7,],[]), False),
    5: (([2,4,6], [8,10,12]), True),
}