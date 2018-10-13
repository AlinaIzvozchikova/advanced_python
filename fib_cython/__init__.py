import pyximport
pyximport.install()

import sys
import os

os.chdir(os.path.dirname(__file__))
sys.path.append(os.getcwd())

import run_cython

fib_function = run_cython.fib
