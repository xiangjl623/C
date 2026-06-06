#include <stdio.h>
#include <stdlib.h>

int main() {
    // calloc浼氬皢鍐呭瓨鍒濆鍖栦负0
    int *arr = (int *)calloc(5, sizeof(int));
    
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);  // 杈撳嚭锛? 0 0 0 0
    }
    printf("\n");
    
    free(arr);
    
    return 0;
}
