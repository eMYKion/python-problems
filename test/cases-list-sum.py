lists = [
    ([],[]),
    (list(range(10)), list(range(10,20))),
    (list(range(20-1,9,-1)), list(range(10,20))),
    (list(range(10,20)), list(range(-10,-20,-1))),
]

cases = {i:(p, list(map(lambda x: x[0] + x[1], zip(*p)))) for i,p in enumerate(lists)}
