#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyObject: not a list\n");
		return;
	}

	Py_ssize_t size = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;

		printf("Element %zd: %s\n", i, type);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyObject: not a bytes object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("[.] Size: %zd\n", size);
	printf("[.] First %zd bytes: ", size > 10 ? 10 : size);

	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < (size > 10 ? 9 : size - 1))
			printf(" ");
	}
	printf("\n");
}

int main(void)
{
	PyObject *list_obj = PyList_New(3);
	PyObject *bytes_obj = PyBytes_FromStringAndSize("Hello, World!", 13);
	PyObject *not_a_list = PyUnicode_FromString("Not a list");

	PyList_SetItem(list_obj, 0, PyUnicode_FromString("Element 0"));
	PyList_SetItem(list_obj, 1, PyLong_FromLong(42));
	PyList_SetItem(list_obj, 2, PyFloat_FromDouble(3.14));

	print_python_list(list_obj);
	print_python_bytes(bytes_obj);
	print_python_list(not_a_list);  /* Should print an error */
	print_python_bytes(not_a_list);  /* Should print an error */

	/* Cleanup */
	Py_XDECREF(list_obj);
	Py_XDECREF(bytes_obj);
	Py_XDECREF(not_a_list);

	return (0);
}

