import importlib
import os
import sys
import itertools
import argparse
import copy #deepcopy

def get_args():
    parser = argparse.ArgumentParser(description='Runs some test cases')
    parser.add_argument('filename')
    args = parser.parse_args()
    return args

def test(filename):
    #filename = os.path.basename(__file__)
    
    #module_name = '-'.join(module_name.split('-')[1:])
    module_name = '.'.join(filename.split('.')[:-1])
    module = importlib.import_module(module_name)
    cases_module = importlib.import_module("test.cases-" + module_name)
    cases = cases_module.cases

    all_correct = True
    for i, pair in cases.items():
        args = pair[0]
        sol = pair[1]
        tst = module.solution(*(copy.deepcopy(args)))
        if tst != sol:
            print("FAILED TEST CASE(%d): for input=%r\n\texpected %r(%s) \
but got %r(%s)\n" \
                  % (i, args, sol, type(sol).__name__, tst, type(tst).__name__))
            all_correct = False
    if (all_correct):
        print("PASS: all test cases passed!")


if __name__ == "__main__":
    args = get_args()
    test(args.filename)
