#include <stdio.h>

int main() {
    printf("Hello");  // 涓嶄細绔嬪嵆杈撳嚭锛岀暀鍦ㄧ紦鍐插尯
    printf(" ");      // 涓嶄細绔嬪嵆杈撳嚭
    printf("World!\n"); // 閬囧埌鎹㈣绗︼紝鍒锋柊缂撳啿鍖猴紝杈撳嚭"Hello World!"
    
    // 鎴栬€呮墜鍔ㄥ埛鏂?    printf("Hello");
    fflush(stdout);   // 鎵嬪姩鍒锋柊缂撳啿鍖?    
    return 0;
}
