#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
} Array;

Array* createArray(int size) {
    Array *arr = (Array *)malloc(sizeof(Array));
    arr->data = (int *)malloc(size * sizeof(int));
    arr->size = size;
    return arr;
}

void destroyArray(Array *arr) {
    free(arr->data);
    free(arr);
}

int main() {
    Array *arr = createArray(10);
    // 浣跨敤arr...
    destroyArray(arr);  // 涓€娆℃€ч噴鏀炬墍鏈夎祫婧?    
    return 0;
}
