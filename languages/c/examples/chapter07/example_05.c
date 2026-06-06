#include <stdio.h>

int main() {
    int num;
    
    do {
        printf("璇疯緭鍏ヤ竴涓鏁帮細");
        scanf("%d", &num);
    } while (num <= 0);
    
    printf("浣犺緭鍏ョ殑姝ｆ暟鏄細%d\n", num);
    
    return 0;
}
