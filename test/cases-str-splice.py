strings = [
    ("",0,0),
    ("hello there",0,0),
    ("hello there", 0, 5),
    ("this is a test", 10, 14),
    ("want a cookie?", 5,6),
    ("0123456789", 4,7),
    ("abcdefghijklmnopqrstuvwxyz", 12,20),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3,9),
    ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ', 6, 16),
]

cases = {
    i: (t,t[0][t[1]:t[2]]) for i,t in enumerate(strings)
}
