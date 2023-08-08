ranges = [
    ((10,15), 0),
    ((10,20,2), 4),
    ((20,30,2), 2),
    ((0,30,3), 8),
    ((0,12), 11),
]


lists = [(list(range(*(args[0]))),args[1]) for args in ranges]
hlists = [(x[0:i]+x[i+1:len(x)], x[i]) for x,i in lists]

cases = {
    i: (p,lists[i][0]) for i,p in enumerate(hlists)
}
