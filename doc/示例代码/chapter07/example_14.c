#include <stdio.h>

int main() {
    int n = 5;
    
    for (int i = 1; i <= n; i++) {
        // 鎵撳嵃绌烘牸
        for (int j = n - i; j > 0; j--) {
            printf(" ");
        }
        // 鎵撳嵃鏄熷彿
        for (int k = 1; k <= 2 * i - 1; k++) {
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}
