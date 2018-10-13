"""
Calculate n-th Fibonacci number using:
Python
C extension
Cython
C using ctypes
Write down timing results in the PR description.

python_fib_result: 1.0049848699569701 seconds
c_fib_result: 0.0065959453582763675 seconds
c_ext_fib_result: 0.007095627784729004 seconds
cython_fib_result: 0.22514170169830322 seconds

After this test - winners are clean C realization and realization on C with Python.h extension
"""

import time

from fib_python.fib import fib as python_fib
from fib_c import fib_function as c_fib
from fib_c_ext import fib_function as c_ext_fib
from fib_cython import fib_function as cython_fib


N = 30  # fib number
CHECK_COUNT = 50  # to get average spend time


def get_general_time(fib_function):
    start_time = time.time()
    for i in range(CHECK_COUNT):
        fib_function(N)
    finish_time = time.time()
    return (finish_time - start_time) / float(CHECK_COUNT)


if __name__ == '__main__':
    python_fib_result = get_general_time(python_fib)
    print("python_fib_result: {} seconds".format(python_fib_result))

    c_fib_result = get_general_time(c_fib)
    print("c_fib_result: {} seconds".format(c_fib_result))

    c_ext_fib_result = get_general_time(c_ext_fib)
    print("c_ext_fib_result: {} seconds".format(c_ext_fib_result))

    cython_fib_result = get_general_time(cython_fib)
    print("cython_fib_result: {} seconds".format(cython_fib_result))
