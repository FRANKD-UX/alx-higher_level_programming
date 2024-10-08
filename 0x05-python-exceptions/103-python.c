#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python list objects.
 * @p: Pointer to a Python object (expected to be a list).
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Python list info\n");
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
    }
}

/**
 * print_python_bytes - Prints information about Python bytes objects.
 * @p: Pointer to a Python object (expected to be bytes).
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *bytes_string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes_string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes_string);
    printf("  first %zd bytes:", (size > 10) ? 10 : size + 1);

    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)bytes_string[i]);

    printf("\n");
}

/**
 * print_python_float - Prints information about Python float objects.
 * @p: Pointer to a Python object (expected to be a float).
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("  value: %f\n", value);
}

