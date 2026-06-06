#include <stdio.h>

int *createArray(int size) {
    // 浣跨敤鍔ㄦ€佸唴瀛樺垎閰?    int *arr = (int *)malloc(size * sizeof(int));
    
    for (int i = 0; i < size; i++) {
        arr[i] = i + 1;
    }
    
    return arr;
}

int main() {
    int *arr = createArray(5);
    
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    free(arr);  // 閲婃斁鍔ㄦ€佸垎閰嶇殑鍐呭瓨
    
    return 0;
}
