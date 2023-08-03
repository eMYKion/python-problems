strings = [
    "the watch and the sky",
    "the bright blue ball",
    "sometimes it happens",
    "life is like a box of chocolates",
    "tear down this wall!",
]

cases = {
    i: ((s,),s.split(" ")[-1]) for i,s in enumerate(strings)
}
