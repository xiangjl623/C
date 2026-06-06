#include <stdio.h>

int main() {
    int a = 5, b = 5;
    int c, d;
    
    // 鍓嶇紑鑷锛氬厛鍔?锛屽啀浣跨敤
    c = ++a;
    printf("鍓嶇紑鑷: a = %d, c = %d\n", a, c);  // a=6, c=6
    
    // 鍚庣紑鑷锛氬厛浣跨敤锛屽啀鍔?
    d = b++;
    printf("鍚庣紑鑷: b = %d, d = %d\n", b, d);  // b=6, d=5
    
    return 0;
}
