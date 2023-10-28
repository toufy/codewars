// Sum of two lowest positive integers
// https://www.codewars.com/kata/558fc85d8fd1938afb000014

#include <stddef.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}
long sum_two_smallest_numbers(size_t n, int numbers[n])
{
    qsort(numbers, n, sizeof(int), compare);
    return (long)numbers[0] + (long)numbers[1];
}
