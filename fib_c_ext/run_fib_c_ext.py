import sys
import os

os.chdir(os.path.dirname(__file__))
sys.path.append(os.getcwd())

import FibonacciExt

asdf = FibonacciExt.fibonacci(20)

print(asdf)