#include <python.h>

static PyObject* spam_strtoint(PyObject* self, PyObject* args) {
	char* str;
	int str_l;

	if (!PyArg_ParseTuple(args, "s", &str))
		return NULL;
	str_l = atoi(str_l);
	return Py_BuildValue("i", str_l);
}

static PyMethodDef SpamMethods[] = {
	{"strtoint", spam_strtoint, METH_VARARGS, "string change int"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",
	"It is a module.",
	-1, SpamMethods
};

PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spammodule); //2. spammodule 구조체참조
}