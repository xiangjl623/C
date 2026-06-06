#include <stdio.h>

int main() {
    int num;
    
    printf("璇疯緭鍏ヤ竴涓暣鏁帮細");
    scanf("%d", &num);
    
    if (num % 2 == 0) {
        printf("%d鏄伓鏁癨n", num);
    } else {
        printf("%d鏄鏁癨n", num);
    }
    
    return 0;
}
