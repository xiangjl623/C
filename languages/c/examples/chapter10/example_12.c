#include <stdio.h>
#include <stdlib.h>

int main() {
    // calloc锛氬垎閰嶅苟鍒濆鍖栦负0
    int *arr1 = (int *)calloc(5, sizeof(int));
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr1[i]);  // 杈撳嚭锛? 0 0 0 0
    }
    printf("\n");
    
    // realloc锛氶噸鏂板垎閰嶅唴瀛?    int *arr2 = (int *)malloc(3 * sizeof(int));
    arr2[0] = 1; arr2[1] = 2; arr2[2] = 3;
    
    arr2 = (int *)realloc(arr2, 5 * sizeof(int));
    arr2[3] = 4; arr2[4] = 5;
    
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr2[i]);  // 杈撳嚭锛? 2 3 4 5
    }
    printf("\n");
    
    free(arr1);
    free(arr2);
    
    return 0;
}
