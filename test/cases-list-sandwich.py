lists = [
    ([1,2,3],[7,7,7,7]),
    ([1],[43, 1]),
    ([],[10, 8, 6]),
]

cases = { i:(p,p[0] + p[1] + p[0]) for i,p in enumerate(lists) }
