#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int capacity;
} DynamicArray;

DynamicArray* createDynamicArray(int initialCapacity) {
    DynamicArray *arr = (DynamicArray *)malloc(sizeof(DynamicArray));
    arr->data = (int *)malloc(initialCapacity * sizeof(int));
    arr->size = 0;
    arr->capacity = initialCapacity;
    return arr;
}

void addElement(DynamicArray *arr, int element) {
    if (arr->size >= arr->capacity) {
        // 鎵╁睍瀹归噺
        arr->capacity *= 2;
        arr->data = (int *)realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size++] = element;
}

void destroyDynamicArray(DynamicArray *arr) {
    free(arr->data);
    free(arr);
}

int main() {
    DynamicArray *arr = createDynamicArray(2);
    
    addElement(arr, 10);
    addElement(arr, 20);
    addElement(arr, 30);  // 瑙﹀彂鎵╁
    
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);  // 杈撳嚭锛?0 20 30
    }
    printf("\n");
    
    destroyDynamicArray(arr);
    
    return 0;
}
