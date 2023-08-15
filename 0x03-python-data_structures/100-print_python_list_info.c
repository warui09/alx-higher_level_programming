#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *itemType = item->ob_type->tp_name;
		
		printf("Element %ld: %s\n", i, itemType);
	}
}

int main(void)
{
	return (0);
}

