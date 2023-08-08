strings = [
    ("hello there", " there"),
    ("akbar and birbal"," and birbal"),
    ("red, white, and blue",", white,"),
    ("ten thousand leagues under the sea","thousand "),
]

cases = {
    i: (p,p[0].replace(p[1], "", 1)) for i,p in enumerate(strings)   
}
