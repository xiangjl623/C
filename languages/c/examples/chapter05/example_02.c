#include <stdio.h>

int main() {
    int a = 10, b = 3;
    float c = 10.0f, d = 3.0f;
    
    printf("鏁存暟闄ゆ硶: %d / %d = %d\n", a, b, a / b);
    printf("娴偣闄ゆ硶: %.1f / %.1f = %.6f\n", c, d, c / d);
    
    // 浣跨敤寮哄埗杞崲瀹炵幇娴偣闄ゆ硶
    printf("寮哄埗杞崲: %d / %d = %.6f\n", a, b, (float)a / b);
    
    return 0;
}
