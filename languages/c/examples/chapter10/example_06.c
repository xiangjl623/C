#include <stdio.h>

// 浣跨敤鎸囬拡浜ゆ崲涓や釜鏁存暟
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    
    printf("浜ゆ崲鍓嶏細x = %d, y = %d\n", x, y);
    
    swap(&x, &y);
    
    printf("浜ゆ崲鍚庯細x = %d, y = %d\n", x, y);
    
    return 0;
}
