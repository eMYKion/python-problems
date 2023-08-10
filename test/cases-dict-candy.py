from collections import Counter

lists = [
    ["M&Ms", "Skittles", "M&Ms", "Starburst", "Starburst"],
    ["Snickers","Sour Patch Kids", "Hershey's Kisses", "Sour Patch Kids",
     "Snickers","Snickers", "Tootsie Pops"],
    ["A","A","B","B","C","B","C","D"],
    ["X","W","W","Y","Z","Z","Z"],
]

cases = {
    i: ((l,), dict(Counter(l))) for i,l in enumerate(lists)
}
