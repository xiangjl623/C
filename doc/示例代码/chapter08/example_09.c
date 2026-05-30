#include <stdio.h>

int main() {
    int arr[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    
    printf("鏁扮粍鍏冪礌鍙婂叾鍦板潃锛歕n");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("arr[%d][%d] = %d, 鍦板潃 = %p\n", i, j, arr[i][j], &arr[i][j]);
        }
    }
    
    return 0;
}
