cases = {
    0: (("",), True),
    1: (("a",), True),
    2: (("aa",), True),
    3: (("aba",), True),
    4: (("ab",), False),
    5: (("abc",), False),
    6: (("abaabaaba",), True),
    7: (("bbabaabbaababb",), True),    
}
