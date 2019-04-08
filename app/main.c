#include <stdio.h>

#include "testlib.h"

int main (void)
{
	int a, b, r;
	a = 10;
	b = 8;
	r = testlib_a_plus_b(a, b);
	printf("a=%d, b=%d, a+b=%d\n", a, b, r);
	return 0;
}