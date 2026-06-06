#include <stdio.h>

int main() {
    int a = 10, b = 20;
    
    // 姹傛渶澶у€?    int max = (a > b) ? a : b;
    printf("鏈€澶у€? %d\n", max);  // 20
    
    // 姹傛渶灏忓€?    int min = (a < b) ? a : b;
    printf("鏈€灏忓€? %d\n", min);  // 10
    
    // 鍒ゆ柇鏄惁涓哄伓鏁?    printf("%d鏄?s\n", a, (a % 2 == 0) ? "鍋舵暟" : "濂囨暟");  // 鍋舵暟
    
    return 0;
}
