#include <stdio.h>

int main() {
    int x = 10;
    
    // 鍒ゆ柇濂囧伓鎬?    if (x & 1) {
        printf("%d 鏄鏁癨n", x);
    } else {
        printf("%d 鏄伓鏁癨n", x);
    }
    
    // 浜ゆ崲涓や釜鏁帮紙涓嶄娇鐢ㄤ复鏃跺彉閲忥級
    int a = 5, b = 7;
    printf("浜ゆ崲鍓? a = %d, b = %d\n", a, b);
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    printf("浜ゆ崲鍚? a = %d, b = %d\n", a, b);
    
    // 蹇€熻绠?鐨勫箓娆?    printf("2^5 = %d\n", 1 << 5);  // 32
    
    return 0;
}
