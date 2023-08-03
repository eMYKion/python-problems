strings = [
    ("", ""),
    ("", "tables"),
    ("hello", ""),
    ("hello", "hello"),
    ("the ", "best"),
    ("how are ", "these cakes?"),
    ("one fish two fish ", "red fish blue fish"),
]


cases = {
    i: (p,len(p[0])+len(p[1])) for i,p in enumerate(strings)
}
