#include <stdio.h>
#include <stdlib.h>

int main() {
    // 鍒嗛厤鍗曚釜鍏冪礌
    int *p = (int *)malloc(sizeof(int));
    if (p == NULL) {
        printf("鍐呭瓨鍒嗛厤澶辫触\n");
        return 1;
    }
    *p = 100;
    printf("*p = %d\n", *p);
    free(p);
    
    // 鍒嗛厤鏁扮粍
    int *arr = (int *)malloc(5 * sizeof(int));
    if (arr == NULL) {
        printf("鍐呭瓨鍒嗛厤澶辫触\n");
        return 1;
    }
    for (int i = 0; i < 5; i++) {
        arr[i] = i;
    }
    free(arr);
    
    return 0;
}
