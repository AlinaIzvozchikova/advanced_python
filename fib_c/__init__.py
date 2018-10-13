from ctypes import CDLL
import os

lb = CDLL(os.path.abspath("fib_c/fibonacci_c.dll"))
fib_function = lb.fibonacci
