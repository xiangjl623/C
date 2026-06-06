#include <stdio.h>

void printArray(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void modifyArray(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        arr[i] *= 2;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    printf("鍘熸暟缁勶細");
    printArray(arr, len);
    
    modifyArray(arr, len);
    
    printf("淇敼鍚庯細");
    printArray(arr, len);
    
    return 0;
}
