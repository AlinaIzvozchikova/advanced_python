"""
    Homework for Advanced Python course.
    Task: Write scipt which causes segmentation fault(python3).
"""

import ctypes
import sys


def crash_using_ctypes(start_bool_value):
    """Crash python using ctypes lib.

    :param start_bool_value: bool start value

    """

    bool_var = ctypes.c_bool(start_bool_value)
    bool_pointer = ctypes.pointer(bool_var)

    for i in range(10000):
        bool_pointer[i] = bool_var


def crash_using_recursion_limit(recursion_limit):
    """Resource exhaustion crash the python interpreter.

    :param recursion_limit: integer value for recursion limit

    """

    sys.setrecursionlimit(recursion_limit)

    def rec_function(rec_function):
        return rec_function(rec_function)

    rec_function(rec_function)


if __name__ == '__main__':
    crash_using_recursion_limit(10000)
    # crash_using_ctypes(True)
