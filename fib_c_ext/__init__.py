import sys
import os

os.chdir(os.path.dirname(__file__))
sys.path.append(os.getcwd())

import FibonacciExt
fib_function = FibonacciExt.fibonacci
