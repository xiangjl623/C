#include <stdio.h>

union FloatBits {
    float f;
    unsigned int i;
};

void printFloatBits(float num) {
    union FloatBits fb;
    fb.f = num;
    
    printf("娴偣鏁帮細%.6f\n", num);
    printf("浜岃繘鍒惰〃绀猴細");
    
    for (int j = 31; j >= 0; j--) {
        printf("%d", (fb.i >> j) & 1);
        if (j == 31 || j == 23) printf(" ");
    }
    printf("\n");
}

int main() {
    printFloatBits(3.14f);
    printFloatBits(-2.5f);
    printFloatBits(0.0f);
    
    return 0;
}
