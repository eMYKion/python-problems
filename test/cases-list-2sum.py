from itertools import product

pairs = [
    ([], 10),
    ([2,7,11,15], 9),
    ([3,2,4], 6),
    ([3,3], 6),
    ([3,2,3],6)
]

#unique "product": (i,j): i < j
def uprod(n):
    return filter(
        lambda x: x[0] < x[1],
        product(range(n), repeat=2)
        )

ans = [
    (
        list(filter(
                lambda ls: ls[1]==l[1],
                [((i,j),l[0][i]+l[0][j]) for i,j in uprod(len(l[0]))])
            ),
        l[1]
    )
    for l in pairs
]

ans = map(lambda x: list(x[0][0][0]) if x[0]!=[] else [] , ans)


cases = {
    i: (arg,sol) for i,(arg,sol) in enumerate(zip(pairs, ans))
}


