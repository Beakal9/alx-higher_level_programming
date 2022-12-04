#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(Pyobject *p)
{
	long int size = PyList_Size(p):
		int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] size of the python list = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_Type(obj->ob_item[i])->tp_name);
}
