#include <stdio.h>

// 棰滆壊琛ㄧず锛堜娇鐢ㄤ綅鍩燂級
struct Color {
    unsigned int red : 8;
    unsigned int green : 8;
    unsigned int blue : 8;
    unsigned int alpha : 8;
};

int main() {
    struct Color c = {255, 128, 64, 255};
    
    printf("绾㈣壊锛?u\n", c.red);
    printf("缁胯壊锛?u\n", c.green);
    printf("钃濊壊锛?u\n", c.blue);
    printf("閫忔槑搴︼細%u\n", c.alpha);
    
    // 灏嗙粨鏋勪綋杞崲涓?2浣嶆暣鏁?    unsigned int color_value = *(unsigned int *)&c;
    printf("棰滆壊鍊硷細0x%08X\n", color_value);
    
    return 0;
}
