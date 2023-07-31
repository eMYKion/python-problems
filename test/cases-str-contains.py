pairs = [
    ("cat in the hat", "hat"),
    ("cat in the hat", "bat"),
    ("abcdefg", "x"),
    ("dogs play", "dog"),
    ("dogs play", "whine"),
]

cases = { i:((s,w), w in s) for i,(s,w) in enumerate(pairs)}
