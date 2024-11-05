#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A PyObject pointer to the Python string object.
 *
 * If the object is not a string, it prints an error message.
 * If the string is compact ASCII or Unicode, it prints the length and value.
 */
void print_python_string(PyObject *p)
{
	long int length;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);

	printf("  type: ");
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("compact ascii\n");
	}
	else
	{
		printf("compact unicode object\n");
	}

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}

