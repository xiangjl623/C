#include <stdio.h>

int main() {
    unsigned char a = 0b00111000;  // 56
    unsigned char b = 0b00011100;  // 28
    
    printf("a = %d (0b%08b)\n", a, a);
    printf("b = %d (0b%08b)\n", b, b);
    printf("a & b = %d (0b%08b)\n", a & b, a & b);  // 鎸変綅涓?    printf("a | b = %d (0b%08b)\n", a | b, a | b);  // 鎸変綅鎴?    printf("a ^ b = %d (0b%08b)\n", a ^ b, a ^ b);  // 鎸変綅寮傛垨
    printf("~a = %d (0b%08b)\n", ~a & 0xFF, ~a & 0xFF);  // 鎸変綅鍙栧弽
    printf("a << 2 = %d (0b%08b)\n", a << 2, a << 2);     // 宸︾Щ
    printf("a >> 2 = %d (0b%08b)\n", a >> 2, a >> 2);     // 鍙崇Щ
    
    return 0;
}
