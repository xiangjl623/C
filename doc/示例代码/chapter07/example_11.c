#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // 璺宠繃鍋舵暟
        }
        printf("%d ", i);
    }
    printf("\n");
    
    return 0;
}
