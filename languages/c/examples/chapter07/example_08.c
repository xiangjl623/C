#include <stdio.h>

int main() {
    int n;
    printf("璇疯緭鍏ヤ竴涓鏁存暟锛?);
    scanf("%d", &n);
    
    int factorial = 1;
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    
    printf("%d鐨勯樁涔樻槸锛?d\n", n, factorial);
    
    return 0;
}
