lens_miss = [
    (10, 3),
    (20, 19),
    (15, 0),
    (5, 2),
    (17, 15),
]

lists_miss = map(lambda x: (list(range(x[0])), x[1]), lens_miss)

cases = {
    i: ((l[0:m]+l[m+1:],),m) for i,(l,m) in enumerate(lists_miss)
}
