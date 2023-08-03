lists = [
    list(range(10)),
    list(range(20)),
    list(range(20,50,5)),
    list(range(10,-10,-1)),
]

cases = {i:((p,),p[::-1]) for i,p in enumerate(lists)}
