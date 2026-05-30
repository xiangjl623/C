#include <stdio.h>

int main() {
    int i = 10;
    float f = 3.14f;
    
    // 闅愬紡杞崲锛歩nt -> float
    float result = i + f;  // i琚浆鎹负float
    printf("result: %f\n", result);  // 杈撳嚭13.140000
    
    // 闅愬紡杞崲锛歠loat -> int锛堟埅鏂皬鏁伴儴鍒嗭級
    int truncated = i + f;  // 缁撴灉13.14琚埅鏂负13
    printf("truncated: %d\n", truncated);  // 杈撳嚭13
    
    return 0;
}
