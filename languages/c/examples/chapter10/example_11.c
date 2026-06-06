#include <stdio.h>
#include <stdlib.h>

int main() {
    // 鍒嗛厤鍗曚釜鏁存暟
    int *p1 = (int *)malloc(sizeof(int));
    *p1 = 42;
    printf("p1 = %d\n", *p1);
    
    // 鍒嗛厤鏁扮粍
    int *arr = (int *)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }
    
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // 閲婃斁鍐呭瓨
    free(p1);
    free(arr);
    
    return 0;
}
