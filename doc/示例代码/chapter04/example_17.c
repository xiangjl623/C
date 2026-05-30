#include <stdio.h>

int x = 10;  // 鍏ㄥ眬鍙橀噺

void func1() {
    int x = 20;  // 灞€閮ㄥ彉閲忥紝闅愯棌鍏ㄥ眬鍙橀噺
    printf("func1: x = %d\n", x);
}

void func2() {
    printf("func2: x = %d\n", x);  // 浣跨敤鍏ㄥ眬鍙橀噺
}

int main() {
    printf("main: x = %d\n", x);   // 浣跨敤鍏ㄥ眬鍙橀噺
    func1();
    func2();
    
    {
        int x = 30;  // 鍧楃骇鍙橀噺
        printf("block: x = %d\n", x);
    }
    
    printf("main: x = %d\n", x);   // 鍥炲埌鍏ㄥ眬鍙橀噺
    
    return 0;
}
