#include <stdio.h>

int main() {
    int n;
    printf("璇疯緭鍏ユ枑娉㈤偅濂戞暟鍒楃殑椤规暟锛?);
    scanf("%d", &n);
    
    int a = 0, b = 1;
    
    for (int i = 1; i <= n; i++) {
        printf("%d ", a);
        int temp = a + b;
        a = b;
        b = temp;
    }
    printf("\n");
    
    return 0;
}
