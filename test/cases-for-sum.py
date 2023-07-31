lists = [
    list(range(10)),
    list(range(5, 11)),
    list(range(3, 20, 2)),
    list(range(20))
]

cases = { i:((k,),sum(k)) for i,k in enumerate(lists)}
