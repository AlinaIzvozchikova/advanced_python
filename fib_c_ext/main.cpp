#include <Python.h>

int fib(int n) {
	if (n < 3) {
		return 1;
	}
	return fib(n - 1) + fib(n - 2);
}

static PyObject* fibonacci(PyObject* self, PyObject* args) {

	int n = 1;
	PyArg_ParseTuple(args, "i", &n);
	int res = fib(n);

	return Py_BuildValue("i", res);
}

static PyMethodDef fibonacci_funcs[] = {
   {
	   "fibonacci",
	   (PyCFunction)fibonacci,
	   METH_VARARGS,
	   "Hello Python"
   },
   {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
	   PyModuleDef_HEAD_INIT,
	   "fibonacci",
	   NULL,
	   -1,
	   fibonacci_funcs
};

PyMODINIT_FUNC  PyInit_FibonacciExt(void) {
	return PyModule_Create(&moduledef);
}