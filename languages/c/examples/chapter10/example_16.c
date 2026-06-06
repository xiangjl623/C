#include <stdio.h>

void reverseArray(int arr[], int len) {
    int *start = arr;
    int *end = arr + len - 1;
    
    while (start < end) {
        int temp = *start;
        *start = *end;
        *end = temp;
        
        start++;
        end--;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    printf("鍘熸暟缁勶細");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    reverseArray(arr, len);
    
    printf("閫嗗簭鍚庯細");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
