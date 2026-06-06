#include <stdio.h>

// 鏁扮粍浣滀负鍑芥暟鍙傛暟
void printArray(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// 淇敼鏁扮粍鍏冪礌
void doubleArray(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        arr[i] *= 2;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    printf("鍘熸暟缁勶細");
    printArray(arr, len);
    
    doubleArray(arr, len);
    
    printf("缈诲€嶅悗锛?);
    printArray(arr, len);
    
    return 0;
}
