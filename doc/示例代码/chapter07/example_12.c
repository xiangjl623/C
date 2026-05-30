#include <stdio.h>

int main() {
    int i = 1;
    
start:
    if (i <= 5) {
        printf("%d ", i);
        i++;
        goto start;  // 璺宠浆鍒皊tart鏍囩
    }
    printf("\n");
    
    return 0;
}
