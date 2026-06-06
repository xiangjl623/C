#include <stdio.h>

// 璁＄畻涓や釜鏁扮殑鍜?int add(int a, int b) {
    return a + b;
}

// 璁＄畻涓や釜鏁扮殑鏈€澶у€?int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int sum = add(5, 3);
    printf("5 + 3 = %d\n", sum);
    
    int maximum = max(10, 15);
    printf("鏈€澶у€硷細%d\n", maximum);
    
    return 0;
}
