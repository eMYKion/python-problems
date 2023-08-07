strings = [
    "hello there",
    "aa bb ",
    "this is a sentence",
    "going on a trip",
]

cases = {
    i: ((s,),max(s, key=lambda x: s.count(x))) for i,s in enumerate(strings)
}
