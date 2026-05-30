#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = (int *)malloc(3 * sizeof(int));
    arr[0] = 1; arr[1] = 2; arr[2] = 3;
    
    // 鎵╁睍鏁扮粍澶у皬
    arr = (int *)realloc(arr, 5 * sizeof(int));
    arr[3] = 4; arr[4] = 5;
    
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);  // 杈撳嚭锛? 2 3 4 5
    }
    printf("\n");
    
    free(arr);
    
    return 0;
}
