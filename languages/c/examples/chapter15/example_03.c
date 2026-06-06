#include <stdlib.h>

int* createArray(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    return arr;
}
