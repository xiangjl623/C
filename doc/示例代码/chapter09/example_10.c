#include <stdio.h>

// 璁＄畻闃朵箻鐨勯€掑綊鍑芥暟
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;  // 閫掑綊缁堟鏉′欢
    }
    return n * factorial(n - 1);  // 閫掑綊璋冪敤
}

int main() {
    int num = 5;
    printf("%d鐨勯樁涔樻槸锛?d\n", num, factorial(num));
    
    return 0;
}
