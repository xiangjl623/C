#include <stdio.h>

int main() {
    int num;
    printf("璇疯緭鍏ヤ竴涓鏁存暟锛?);
    scanf("%d", &num);
    
    if (num <= 1) {
        printf("%d涓嶆槸璐ㄦ暟\n", num);
        return 0;
    }
    
    int is_prime = 1;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            is_prime = 0;
            break;
        }
    }
    
    if (is_prime) {
        printf("%d鏄川鏁癨n", num);
    } else {
        printf("%d涓嶆槸璐ㄦ暟\n", num);
    }
    
    return 0;
}
