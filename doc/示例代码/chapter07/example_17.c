#include <stdio.h>

int main() {
    int a, b;
    printf("璇疯緭鍏ヤ袱涓鏁存暟锛?);
    scanf("%d %d", &a, &b);
    
    // 浣跨敤杈楄浆鐩搁櫎娉?    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    
    printf("鏈€澶у叕绾︽暟鏄細%d\n", a);
    
    return 0;
}
