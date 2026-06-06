#include <stdio.h>

int main() {
    int a = 10;
    int *p = &a;
    
    printf("a = %d\n", a);      // 鐩存帴璁块棶鍙橀噺
    printf("&a = %p\n", &a);    // 鑾峰彇鍙橀噺鍦板潃
    printf("p = %p\n", p);      // 鎸囬拡瀛樺偍鐨勫湴鍧€
    printf("*p = %d\n", *p);    // 閫氳繃鎸囬拡璁块棶鍙橀噺
    
    return 0;
}
