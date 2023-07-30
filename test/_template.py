import importlib
import os
import sys
import itertools
sys.path.append('../')

def test():
    filename = os.path.basename(__file__)
    module_name = filename.split('.')[0]
    module_name = '-'.join(module_name.split('-')[1:])
    module = importlib.import_module(module_name, package="python-problems")

    #TODO: write testing function here

if __name__ == "__main__":
    test()
