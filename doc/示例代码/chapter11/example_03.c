#include <stdio.h>
#include <stdlib.h>

int main() {
    // 鍦ㄥ爢涓婂垎閰嶄竴涓暣鏁?    int *p = (int *)malloc(sizeof(int));
    *p = 42;
    printf("p = %d\n", *p);
    
    // 鍦ㄥ爢涓婂垎閰嶄竴涓暟缁?    int *arr = (int *)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }
    
    // 鎵嬪姩閲婃斁鍐呭瓨
    free(p);
    free(arr);
    
    return 0;
}
