#include <stdio.h>

int main() {
    int n = 5;
    
    // 涓婂崐閮ㄥ垎
    for (int i = 1; i <= n; i++) {
        for (int j = n - i; j > 0; j--) {
            printf(" ");
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    
    // 涓嬪崐閮ㄥ垎
    for (int i = n - 1; i >= 1; i--) {
        for (int j = n - i; j > 0; j--) {
            printf(" ");
        }
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}
