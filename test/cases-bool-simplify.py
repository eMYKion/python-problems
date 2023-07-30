cases = {
    (True, True): True,
    (True, False): False,
    (False, True): True,
    (False, False): True,
}

'''import importlib
import os
import sys
import itertools
sys.path.append('../')

def test():
    filename = os.path.basename(__file__)
    module_name = filename.split('.')[0]
    module_name = '-'.join(module_name.split('-')[1:])
    module = importlib.import_module(module_name, package="python-problems")

    all_correct = True
    for arg in itertools.product((True, False), repeat=2):
        ref = module.func(*arg)
        tst = module.func_simple(*arg)
        if ref != tst:
            print("ERROR: expected %s but got %s for args=%s" % (ref, tst, arg))
            all_correct = False
    if (all_correct):
        print("PASS: all test cases passed")

if __name__ == "__main__":
    test()
'''
