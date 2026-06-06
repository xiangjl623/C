#include <stdio.h>

int main() {
    FILE *fp = fopen("example.txt", "r");
    if (fp == NULL) {
        perror("鎵撳紑鏂囦欢澶辫触");
        return 1;
    }
    
    // 鑾峰彇褰撳墠浣嶇疆
    long pos = ftell(fp);
    printf("鍒濆浣嶇疆锛?ld\n", pos);
    
    // 璇诲彇涓€浜涘唴瀹?    char buffer[10];
    fgets(buffer, sizeof(buffer), fp);
    
    // 鑾峰彇褰撳墠浣嶇疆
    pos = ftell(fp);
    printf("璇诲彇鍚庣殑浣嶇疆锛?ld\n", pos);
    
    fclose(fp);
    
    return 0;
}
