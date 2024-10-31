#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A PyObject pointer to the Python string object.
 *
 * If the object is not a string, it prints an error message.
 * If the string cannot be decoded, it also prints an error message.
 */
void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("Error: Invalid String Object\n");
		return;
	}

	Py_ssize_t size;
	const char *str;

	str = PyUnicode_AsUTF8AndSize(p, &size);
	if (str == NULL)
	{
		printf("Error: Unable to decode String Object\n");
		return;
	}

	printf("[.] string object info\n");
	printf("  type: ");
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("compact ascii\n");
	}
	else
	{
		printf("compact unicode object\n");
	}

	printf("  length: %ld\n", size);
	printf("  value: %s\n", str);
}

