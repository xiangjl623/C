#include <stdio.h>

int main() {
    float pi = 3.14159f;
    
    // 鏄惧紡杞崲锛歠loat -> int
    int integer_part = (int)pi;
    printf("鏁存暟閮ㄥ垎: %d\n", integer_part);  // 杈撳嚭3
    
    // 鏄惧紡杞崲锛歩nt -> float
    int num = 5;
    float decimal = (float)num / 2;  // 缁撴灉鏄?.5鑰屼笉鏄?
    printf("5/2 = %f\n", decimal);   // 杈撳嚭2.500000
    
    return 0;
}
