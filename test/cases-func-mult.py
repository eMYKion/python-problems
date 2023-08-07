triples = [
    (3,2,1),
    (33,0,5),
    (1,5.5,67),
    (109, 77, 22),
    ("hello there\n", 3, 2), # ;P
]

cases = {
    i: (t,t[0]*t[1]*t[2]) for i,t in enumerate(triples)
}
