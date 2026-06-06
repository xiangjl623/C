#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    char target;
    int count = 0;
    
    printf("璇疯緭鍏ヤ竴涓瓧绗︿覆锛?);
    fgets(str, sizeof(str), stdin);
    
    printf("璇疯緭鍏ヨ缁熻鐨勫瓧绗︼細");
    scanf("%c", &target);
    
    // 缁熻瀛楃鍑虹幇娆℃暟
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == target) {
            count++;
        }
    }
    
    printf("瀛楃'%c'鍦ㄥ瓧绗︿覆涓嚭鐜颁簡%d娆n", target, count);
    
    return 0;
}
