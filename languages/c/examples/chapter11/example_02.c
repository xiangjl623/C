#include <stdio.h>

void recursiveFunc(int n) {
    char buffer[1024];  // 姣忔閫掑綊鍒嗛厤1KB
    printf("閫掑綊娣卞害锛?d\n", n);
    recursiveFunc(n + 1);  // 鏃犻檺閫掑綊
}

int main() {
    recursiveFunc(1);
    return 0;
}
