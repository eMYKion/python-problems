lists = [
    list(range(10)),
    list(range(10,20)),
    list(range(20,10,-1)),
    [0,1,2,3,5,4,6,7,8,9],
]

cases = {
    i: ((l,), all(l[i]<=l[i+1] for i in range(len(l)-1))) for i,l in enumerate(lists)
}
'''
cases = {
    i: ((l,), l==sorted(l)) for i,l in enumerate(lists)
}
'''
